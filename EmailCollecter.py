import urlparse
import urllib
from sys import argv
from bs4 import BeautifulSoup 
def my_emaillist(homepage, textfile ):

	urlfile = open(textfile,'a')   
	url = homepage
	urls = [url] 
	visited =  [url]
	while len(urls) > 0  :
		try :
			htmltext = urllib.urlopen (urls[0]).read()
		except :
			print urls[0]
		soup = BeautifulSoup(htmltext)
		urls.pop(0)
		for tag in soup.findAll('a',href= True):
			tag['href']= urlparse.urljoin(url ,tag['href'])
			if url in tag['href'] and tag['href'] not in visited:
				urls.append(tag['href'])
				visited.append(tag['href'])
	for i in visited:	
		urlfile.write(str(i+"\n"))	
	urlfile.close()
	
	
if __name__ == "__main__":
	script, url = argv
	my_emaillist(url,"file.txt",)
