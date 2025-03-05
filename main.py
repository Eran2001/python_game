from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
  contents = file.read()
  
soup = BeautifulSoup(contents, "lxml")

print(soup.select(selector="body a"))