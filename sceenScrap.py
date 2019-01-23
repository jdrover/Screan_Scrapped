# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup


raw_html = open('scrape.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
    print(p.text)

# specify the url
#quote_page = open('scrape.html').read()

# query the website and return the html to the variable ‘page’
#page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
#soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
#name_box = soup.find('h1', attrs={'class': 'name'})

#name = name_box.text # strip() is used to remove starting and trailing
#print(name)
