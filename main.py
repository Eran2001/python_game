from bs4 import BeautifulSoup
import lxml
import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

URL = requests.get("https://www.billboard.com/charts/hot-100/2000-08-12/", headers=headers)

response = URL.text

soup = BeautifulSoup(response, "lxml")

heading = soup.find(name="h3")

print(heading.text.strip())

