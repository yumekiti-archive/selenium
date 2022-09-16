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

# Done
print('Done')
