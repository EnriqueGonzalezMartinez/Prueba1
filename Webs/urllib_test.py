from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read().decode(),"\n")

html = urlopen("http://pythonscraping.com/pages/page1.html")
bs = BeautifulSoup(html.read(), features="lxml")
print(bs.html,"\n")
print(bs.html.body.h1)
