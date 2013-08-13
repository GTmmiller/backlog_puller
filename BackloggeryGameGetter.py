import urllib2
import sys
from string import Template

spoofedHeader = {
   'Connection': 'keep-alive', 
   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36',
   'Accept': '*/*',
   'Referer': 'http://backloggery.com/games.php?user=ThatGuy',
   'Accept-Encoding': 'gzip,deflate,sdch',
   'Accept-Language': 'en-US,en;q=0.8'
   }

no_entries = 0   
page_string = ''
opener = urllib2.build_opener()
backloggeryTemplate = Template('http://backloggery.com/ajax_moregames.php?user=ThatGuy&console=&rating=&status=&unplayed=&own=&search=&comments=&region=&region_u=0&wish=&alpha=&temp_sys=ZZZ&total=0&aid=1&ajid=$entries')

backloggeryUrl = backloggeryTemplate.substitute(entries=str(no_entries))
backlogRequest = urllib2.Request(backloggeryUrl, None, spoofedHeader)
print backloggeryUrl
bPage = urllib2.urlopen(backlogRequest)
temp_string = bPage.read()

while temp_string.find('\t<div id="output2">') > -1:
   page_string += temp_string.split('\t<div id="output2">')[0]
   no_entries += 50
   backloggeryUrl = backloggeryTemplate.substitute(entries=str(no_entries))
   backlogRequest = urllib2.Request(backloggeryUrl, None, spoofedHeader)
   print backloggeryUrl
   bPage = urllib2.urlopen(backlogRequest)
   temp_string = bPage.read()
   print 'new request'

page_string += temp_string

save_page = open('proxyget.html', 'w')
save_page.write(page_string)
save_page.close()

print 'Your page was recieved'