import urllib2
from string import Template

class BackloggeryRequester:
   _spoofed_header = {
   'Connection': 'keep-alive', 
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
   'Accept': '*/*',
   'Referer': 'http://backloggery.com/games.php?user=ThatGuy',
   'Accept-Encoding': 'gzip,deflate,sdch',
   'Accept-Language': 'en-US,en;q=0.8'
   }
   _page_request_template = Template('http://backloggery.com/ajax_moregames.php?user=$username&console=&rating=&status=&unplayed=&own=&search=&comments=&region=&region_u=0&wish=&alpha=&temp_sys=ZZZ&total=0&aid=1&ajid=$entries')
   _request_footer = '\t<div id="output2">'   
   def __init__(self, username):
      self.username = username
   def more_games(self, start_point):
      backloggeryUrl = self._page_request_template.substitute(username=self.username, entries=str(start_point))
      backlogRequest = urllib2.Request(backloggeryUrl, None, self._spoofed_header)
      return urllib2.urlopen(backlogRequest).read()
   def get_raw_page(self):
      no_entries = 0
      full_page = ''
      temp_page = self.more_games(no_entries)
      
      while temp_page.find(self._request_footer) > -1:
         full_page += temp_page.split(self._request_footer)[0]
         no_entries += 50
         temp_page = self.more_games(no_entries)
      full_page += temp_page
      return full_page
