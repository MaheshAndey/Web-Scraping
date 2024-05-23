import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://news.ycombinator.com/news")

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')


