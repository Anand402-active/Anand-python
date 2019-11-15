import requests        # requests is used to connect to URL
from bs4 import BeautifulSoup   # Beautiful Soup is a Python library for pulling data out of HTML and XML files
import csv
# with open('1.html') as html_file:
#     soup = BeautifulSoup(html_file,'lxml')
# print(soup.prettify())      # Now soup_prettify is printed, it gives the visual representation of the parse tree created from the raw HTML content.step 4: Searching and navigating through the parse tree.  '''
# match=soup.text
# match=soup.title.text
# print(match)
#
# for article in soup.find_all('div',class_="article"): # this is used to find all the div tags in HTML or XML file
#     headline=article.h2.a.text
#     print(headline)
#
#     summary=article.p.text
#     print(summary)
csv_file=open('csv_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','youtube;ink'])
source = requests.get('http://coreyMS.com').text
soup= BeautifulSoup(source,'lxml')
for article in soup.find_all('article'):
#print(article.prettify())
#print(soup.prettify())
    try:
        headline=article.h2.a.text
        print(headline)

        summary=article.find('div',class_='entry-content').p.text
        print(summary)

        vid_src=article.find('iframe',class_='youtube-player')['src']
        #print(vid_src)
        vi_id=vid_src.split('/')[4]
        vi_id=vi_id.split('?')[0]
        #print(vi_id)


        yt_link=f'https://youtube.com/watch?v={vi_id}'
        print(yt_link)
    except Exception as e:
        yt_link=None
        summary=None
        headline=None
        print(e)
    csv_writer.writerow([headline,summary,yt_link])

    print()
    print()
csv_file.close()
