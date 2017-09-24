from bs4 import BeautifulSoup
import requests
import csv


def get_pages(url):
    # soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    url_text = requests.get(url).url
    print(url_text)


#first 
start_url = 'http://statistics.byuimath.com/index.php?title='

if __name__ == '__main__':
    get_pages(start_url)
