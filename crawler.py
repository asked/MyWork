import urlparse
import urllib
import sys
import re 
from bs4 import BeautifulSoup 
def my_emaillist(homepage, textfile , eamilstext,HTMLfileout ):

	urlfile = open(textfile,'a')  
	emailsfile = open(eamilstext,'a')  
	HTMLfile = open(HTMLfileout,'a')
	url = homepage
	urls = [url] 
	visited =  [url]
	eamils =[]
	visitedemail=[]
	wholetext = []
	while len(urls) > 0  :
		try :
			htmltext = urllib.urlopen (urls[0]).read()
		except :
			print urls[0]
		soup = BeautifulSoup(htmltext)
		urls.pop(0)
		eamils = re.compile( '\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}')
		visitedemail.append("".join( re.findall (eamils,str(soup))))	
		for tag in soup.findAll('a',href= True):
			tag['href']= urlparse.urljoin(url ,tag['href'])
			if url in tag['href'] and tag['href'] not in visited:
				urls.append(tag['href'])
				visited.append(tag['href'])
			
	urlfile.write(str(visited))	
	emailsfile.write(str(visitedemail))
	urlfile.close()
	emailsfile.close()
my_emaillist("http://www.mileycyrus.com","file.txt","eamils.txt","HTMLPage.txt")
