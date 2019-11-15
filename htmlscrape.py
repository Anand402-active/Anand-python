import requests        # requests is used to connect to URL
from bs4 import BeautifulSoup   # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import csv
with open('1.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')
print(soup.prettify())      # Now soup_prettify is printed, it gives the visual representation of the parse tree created from the raw HTML content.step 4: Searching and navigating through the parse tree.  '''
match=soup.text
match=soup.title.text
print(match)

for article in soup.find_all('div',class_="article"): # this is used to find all the div tags in HTML or XML file
    headline=article.h2.a.text
    print(headline)

    summary=article.p.text
    print(summary)
