import urllib2
from string import Template

class GamesRequest:
   """This class requests pages from the backloggery site.

   Using a spoofed header this class pulls games lists in html form from
   a given backloggery page. The only thing it takes as a parameter is a username
   so an object must be made for every username you want to make requests for.
   """
   _spoofed_header = {
   'Connection': 'keep-alive', 
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
   'Accept': '*/*',
   'Referer': '',
   'Accept-Encoding': 'gzip,deflate,sdch',
   'Accept-Language': 'en-US,en;q=0.8'
   }
   _page_request_template = Template('http://backloggery.com/ajax_moregames.php?user=$username')
   _referer_template = Template('http://backloggery.com/games.php?user=$username')
   _more_games_template = Template('&console=&rating=&status=&unplayed=&own=&search=&comments=&region=&region_u=0&wish=&alpha=&temp_sys=ZZZ&total=0&aid=1&ajid=$entries')
   _request_footer = '\t<div id="output2">'   
   
   def __init__(self, username):
      """Construct the Request object for a specific user"""
      self.username = username
      self.request_url = self._page_request_template.substitute(username=self.username)
      self._spoofed_header['Referer'] = self._referer_template.substitute(username=self.username)
      
   def more_games(self, start_point):
      """Perform a call to the backloggery 'more_games' php function to get 50 more games from a specified start point"""
      more_games_url = self.request_url + self._more_games_template.substitute(entries=str(start_point))
      more_games_request = urllib2.Request(more_games_url, None, self._spoofed_header)
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