import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import sys
import os
from time import sleep

titles = []
imgs = []
links = []

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)

# Download the page
url = sys.argv[1]
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'html.parser')

# body
body = soup.find('body')
print(body)


driver.get(url)
driver.implicitly_wait(10)
html = driver.page_source.encode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

# body
body = soup.find('body')
print(body)

# Done
driver.quit()
print('--- Done ---')
