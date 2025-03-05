from bs4 import BeautifulSoup
import lxml

doc = """
<form method="get" action="/search/">
 <input type="text" name="q" maxlength="255" value=""></input>
</form>
"""

with open("website.html") as file:
  contents = file.read()
  
soup = BeautifulSoup(contents, "lxml")

html_doc = BeautifulSoup(doc, "lxml")

print(html_doc.input["maxlength"])

