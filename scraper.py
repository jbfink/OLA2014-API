from bs4 import BeautifulSoup
import urllib2

url = urllib2.urlopen("http://www.imdb.com/title/tt0096256/")
html_content = url.read()
soup = BeautifulSoup(html_content)
length = soup.find("time")

print length.contents
