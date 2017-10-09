#!/usr/local/bin/python

from bs4 import BeautifulSoup
fp = open("t1.html")
soup = BeautifulSoup(fp)
#soup2 = BeautifulSoup("<html>data</html>")
#head = soup1.find("head")

#print(soup1)
#print(head)
#print(soup2)

html = soup.contents[0] # <html> ... </html>
head = html.contents[0] # <head> ... </head>
body = html.contents[1] # <body> ... </body>
body2 = head.nextSibling
body3 = soup.find("body")
head3 = body3.findPreviousSibling
tail33 = body3.findNextSibling
tail = html.contents[2] # <tail> ... </tail>
tail2 = body2.nextSibling
tail3 = soup.find("tail")
body33 = tail3.findPreviousSibling

#print html
#print head
print "follow is head content:"
print head3
print "follow is body content:"
print body33
print "follow is tail content:"
print tail33
