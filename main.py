from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

website = response.text

soup = BeautifulSoup(website, "lxml")

all_movies = soup.find_all(name="h3", class_="title")


movie_title = [movie.getText() for movie in all_movies]
movies = movie_title[::-1]

with open("Movies.txt", "w") as file:
  for movie in movies:
    file.write(f"{movie}\n")