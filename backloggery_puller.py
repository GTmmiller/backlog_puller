import urllib2
import xml.etree.ElementTree as ET
import json
from string import Template
from HTMLParser import HTMLParser


class GamesRequest:
    """This class requests pages from the backloggery site.

    Using a spoofed header this class pulls games lists in html form from
    a given backloggery page. The only thing it takes as a parameter is a
    username so an object must be made for every username you want to make
    requests for.
    """

    _spoofed_header = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
        'Accept': '*/*',
        'Referer': '',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'en-US,en;q=0.8'
    }
    _page_request_template = Template('http://backloggery.com/ajax_moregames.'
                                      'php?user=$username')
    _referer_template = Template('http://backloggery.com/games.php?'
                                 'user=$username')
    _more_games_template = Template('&console=&rating=&status=&unplayed=&own='
                                    '&search=&comments=&region=&region_u=0'
                                    '&wish=&alpha=&temp_sys=ZZZ&total=0&aid=1'
                                    '&ajid=$entries')
    _request_footer = '\t<div id="output2">'

    def __init__(self, username):
        """Construct the Request object for a specific user"""
        self.username = username
        self.request_url = self._page_request_template.substitute(
            username=self.username)
        self._spoofed_header['Referer'] = self._referer_template.substitute(
            username=self.username)

    def more_games(self, start_point):
        """Perform a call to the backloggery 'more_games' AJAX call to get
        50 more games from a specified start point
        """
        more_games_url = self.request_url +
        self._more_games_template.substitute(entries=str(start_point))

        more_games_request = urllib2.Request(
            more_games_url, None, self._spoofed_header)
        return urllib2.urlopen(more_games_request).read()

   def get_raw_page(self):
      """Pull a complete html page containing all of the games and collections in a backloggery account"""
      no_entries = 0
      full_page = ''
      temp_page = self.more_games(no_entries)
      
      while temp_page.find(self._request_footer) > -1:
         full_page += temp_page.split(self._request_footer)[0]
         no_entries += 50
         temp_page = self.more_games(no_entries)
      full_page += temp_page
      return full_page

class CompilationAdder(HTMLParser):
   """A class used to replace compilations with separate games in a backloggery page"""
   def __init__(self):
      HTMLParser.__init__(self)
      
   
class BacklogHTMLParser(HTMLParser):
   """A class used to parse the backloggery html pages"""
   
   def __init__(self):
      HTMLParser.__init__(self)
	  
      #HTML parsing control variables
      self.console_name_found = False
      self.game_block_end = True
      self.in_gamerow = False
      self.found_gamename = False
      #dictionary of len(2) string lists
      self.backlog = {}
      #placeholder variables for system data
      self.current_name = ''
      
   #note to self: error checking should happen eventually
   def handle_starttag(self, tag, attrs):
      if tag == 'section' and attrs[0][1] == 'system title shadow' and self.game_block_end:
         self.console_name_found = True
         self.game_block_end = False
         
      elif tag == 'section' and attrs[0][1] == 'gamebox systemend':
         self.game_block_end = True

      #We're in the gamerow so we can ignore data
      elif tag == 'div' and attrs[0][1] == 'gamerow':
         self.in_gamerow = True

      elif tag == 'b' and self.in_gamerow == False:
         self.found_gamename = True

      elif tag == 'img' and attrs[1][1] == '16' and attrs[2][1] == '16':
         self.backlog[self.current_name].append([attrs[0][1].strip()])
         print '\t', attrs[0][1].strip()
         
   def handle_endtag(self, tag):
      if self.in_gamerow and tag == 'div':
         self.in_gamerow = False
      
   def handle_data(self, data):
      if self.console_name_found:
         self.backlog[data] = []
         self.current_name = data
         print data
         self.console_name_found = False

      #Print the data only if you're in a game box and if the gamerow hasn't
      #been passed yet
      elif not self.game_block_end and self.found_gamename:

         if not data.isspace():

            if len(self.backlog[self.current_name][-1]) == 1:
               self.backlog[self.current_name][-1].append(data.strip())

            else:
               self.backlog[self.current_name].append([data.strip()])
            
            print '\t', data.strip()
            self.found_gamename = False

   #Note to self: throw an error if you have a blank backlog
   def xml_output(self):
      """ This method takes in the backlog dictionary created in the html parser
      and converts it to xml. The schema for the XML will be available
      eventually
      """

      console_names = self.backlog.keys()
         
      root = ET.Element("backlog")
      for console_name in console_names: 
         console = ET.SubElement(root, "console", name=console_name)
         for gamedata_list in self.backlog[console_name]:
            if(len(gamedata_list) == 2):
               game = ET.SubElement(console, "game", completion=gamedata_list[0])
               game.text = gamedata_list[1]
                  
            else:
               game = ET.SubElement(console, "game", completion="(-)")
               game.test = gamedata_list[0]

      ET.dump(root)
      return ET.tostring(root)
	  
   def json_output(self):
      return json.JSONEncoder().encode(self.backlog)
