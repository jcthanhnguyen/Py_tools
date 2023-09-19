import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import termcolor

	
# find all emails appear in the url	
def find_mails(url):
    try:
        data = urllib.request.urlopen(url).read().decode()
    except:
        data = urllib.request.urlopen(url).read().decode('ISO-8859-1')
        
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
    return emails	
 

# def find_mails(data):
# 	data = data.read().decode()
# 	emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', data)
# 	return emails

# find all urls in current url
def find_urls(data):
	soup = BeautifulSoup(data.read(), 'html.parser')
	a_tags = soup('a')
	links = list()
	
	for a in a_tags:
		links += re.findall('href="(http.+?)"', str(a))
	return links
		
# crawl through urls using recursion
def crawl(url, layers):
	try:#Checking for connection and connect
		if layers == 0: return
		print('\n This is layer', layers)
		print(termcolor.colored('[*] URL: ' + url + '\n', 'cyan'))
		data = urllib.request.urlopen(str(url))
	except:
		print(termcolor.colored('!! NO CONNECTION !!', 'red'))
		return
		
	
	links = find_urls(data)	
	if len(links) == 0: 
		print(termcolor.colored('\t[-]', 'red') + ' NO CHILDREN URLS')
			
	mails = find_mails(url)
	if len(mails) == 0: 
		print(termcolor.colored('\t[-]', 'red') + ' NO EMAIL')

	else:
		print(termcolor.colored('\t[+] ', 'green') + 'Emails:')
		for mail in mails:
			print(termcolor.colored('\t\t- '+mail,'blue'))
				
	for link in links:
		crawl(link, layers - 1)

# decide to repeat the crawler or not			
def yes_no():
	while True:
		deci = input('Do you want to continue (y/n): ')
		if deci != 'y' and deci != 'n':
			print(termcolor.colored('\n!! Error Input, Choose Again !!', 'red'))
		else:
			return deci
#main 
print(termcolor.colored('\n***** W3B CR4WL3R *****', 'magenta'))
print(termcolor.colored('---collecting emails---', 'magenta'))

while True:
	url = input('\n[*] Enter your target\'s URL: ')
	layers = int(input('[*] How many layers do you want to crawl: '))
	print('\nCrawling . . .')
	crawl(url, layers)
	deci = yes_no()
	if deci == 'n':
		break