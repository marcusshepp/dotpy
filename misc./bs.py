import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('http://www.mywebsite.com')



links = [link for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')) if link.find("word") != -1]
print links

    