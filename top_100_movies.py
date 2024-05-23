from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century")

website = response.text

soup = BeautifulSoup(website, 'html.parser')


all_movies = soup.find_all(name='h2')
# print(all_movies)


movies = [movie.getText() for movie in all_movies]

movies = movies[1:200:2]


with open('movies.txt', 'w') as file:
    for i in range(len(movies) - 1, -1, -1):
        file.write(f"{100-i}) {movies[i]}\n")