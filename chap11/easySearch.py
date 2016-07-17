#!python3
#easySearch.py-opens several google search results

import requests,sys,webbrowser,bs4

print('Googling...')
res=requests.get('https://www.google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text)
linkelem=soup.select('.r a')
numOpen=min(5,len(linkelem))
for i in range(numOpen):
	webbrowser.open('https://www.google.com'+linkelem[i].get('href'))
