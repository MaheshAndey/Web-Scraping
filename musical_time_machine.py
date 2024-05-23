import requests

from bs4 import BeautifulSoup

response = requests.get(url="https://www.billboard.com/charts/hot-100")

data = response.text

soup = BeautifulSoup(data, 'html.parser')

song_name = soup.find_all(name='span',  class_="chart-element__information__song")

song = [i.getText() for i in song_name]

print(song)


