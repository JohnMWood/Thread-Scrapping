import threading
from bs4 import BeautifulSoup
import requests


def parse_site(url_text):
    soup = BeautifulSoup(requests.get(url_text).text, 'html5lib')
    print(soup.title)


def without_threads(start_url, titles):
    for title in titles:
        parse_site(start_url + title)


def with_threads(start_url, titles):
    threads = []

    for title in titles:
        url = start_url + title # single string for argument

        t = threading.Thread(target=parse_site, args=(url,))
        t.start()
        threads.append(t)

    for th in threads:
        th.join()


titles_list = open('threading_scraping/stats_titles.txt').read()
titles_list = titles_list.replace('\'', '').split(',')

start_url = 'http://statistics.byuimath.com/index.php?title='

if __name__ == '__main__':
    without_threads(start_url, titles_list)
    # with_threads(start_url, titles_list)
