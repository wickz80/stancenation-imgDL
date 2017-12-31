# -*- coding: utf-8 -*-
import random
import time
from bs4 import BeautifulSoup
import requests
import re
import urllib.request

pages_back = 25
base_url = 'http://www.stancenation.com/topics/car-features/page/'
url_list = []

for url in range(3, pages_back):
    url_list += [base_url + str(url)]

desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']
 
def random_headers():
    return {'User-Agent': random.choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
 
article_urls = []
for url in range(0, len(url_list)):
    try:
        print('\nPage:' + str(url+1) + "\n")
        html_content = requests.get(url_list[url], headers=random_headers())
        soup = BeautifulSoup(html_content.text, "html.parser")
        articles = soup.body.div.findAll('div', attrs={'class':'cb-meta clearfix'})
        for article in articles:
            temp = article.h2.a
            print(temp.text)
            temp = str(article.h2.a['href'])
            article_urls += [temp]
            print(temp)
            
        time.sleep(random.uniform(2.50, 5.129))
    except:
        time.sleep(random.uniform(2.50, 5.129))

imglinks = []
imgraw = []
for url in range(0, len(article_urls)):
    try:
        html_content = requests.get(article_urls[url], headers=random_headers())
        soup = BeautifulSoup(html_content.text, "html.parser")
        imgraw = soup.section.findAll('img')
        for img in imgraw:
            imglinks += [img['src']]
        print("opening article #" + str(url))
        time.sleep(random.uniform(.5, 1.2))
    except:
        time.sleep(random.uniform(.5, 1.2))
        
for imglink in range(0, len(imglinks)):
    try:
        urllib.request.urlretrieve(imglinks[imglink], "C:\\stancenaysh\\image" + str(imglink) + ".jpg")
        print("Downloaded" + str(imglink) + "images...")
        time.sleep(random.uniform(2.50, 5.129))
    except:
        time.sleep(random.uniform(2.50, 5.129))