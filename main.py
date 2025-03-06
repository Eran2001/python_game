from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "lxml")
title = soup.find(name="span", class_="titleline")
print(title.get_text())

