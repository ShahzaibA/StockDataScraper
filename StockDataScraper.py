import urllib
import re

symbolfile = open("symbols.txt")
symbolslist = symbolfile.read()


newsymbolslist = symbolslist.split("\n")


i=0
while i<len(newsymbolslist):
	url = "http://www.nasdaq.com/symbol/" + newsymbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<div id="qwidget_lastsale" class="qwidget-dollar">(.+?)</div>'
	pattern = re.compile(regex)
	price = re.findall(pattern, htmltext)
	print "The price of", newsymbolslist[i], "is", price[0]
	i+=1

