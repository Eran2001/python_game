from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup("<p>Some<b>bad<i>HTML", "lxml")
print(soup.prettify())

print(soup.find(string="era"))

