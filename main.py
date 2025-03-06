from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

search = driver.find_element(By.NAME, "q")
print(search.tag_name)

driver.quit()