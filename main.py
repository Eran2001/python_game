from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
  contents = file.read()
  
soup = BeautifulSoup(contents, "lxml")

print(soup.title.text)
print(soup.title.string)

print(soup.a)

print(soup.find_all("a"))

print(soup.find("a").text)

print(soup.find("a")["href"])
