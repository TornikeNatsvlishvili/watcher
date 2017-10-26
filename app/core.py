from app.constants import URLS, HEADERS

from bs4 import BeautifulSoup
import requests
import re
import datetime
import time
import logging


def get_direct_pdf_url(detail_url: str):
    resp = requests.get(detail_url, headers=HEADERS)
    html = resp.text
    soup = BeautifulSoup(html, "lxml")

    dl_link_el = soup.find('a', href=re.compile(r'vk.com/d'))
    return dl_link_el.attrs['href']


def find_articles_since(url: str, date):
    resp = requests.get(url, headers=HEADERS)
    html = resp.text

    soup = BeautifulSoup(html, "lxml")
    article_headers = soup.find_all(class_='entry-header')
    article_detail_links = soup.find_all(class_='g1-frame')
    for header, detail_link in zip(article_headers, article_detail_links):
        str_pub_date = re.search(r'datetime="(.*?)">', str(header)).group(1)
        pub_date = datetime.datetime.strptime(
            str_pub_date, '%Y-%m-%dT%H:%M:%S')
        title = header.find(class_="entry-title").text

        if pub_date > date:
            detail_page_url = detail_link.attrs['href']
            direct_pdf_url = get_direct_pdf_url(detail_page_url)
            return title, direct_pdf_url

    return None

def scan_urls(start_date):
    magazines = []
    for url, name in URLS:
        res = find_articles_since(url, start_date)
        if res:
            magazines.append((res[0], res[1]))
            logging.info(f'Done {res[0]}')

        time.sleep(1)

    return magazines
