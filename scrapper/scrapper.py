import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json

url = "https://www.nba.com/stats/players/traditional"

# instanciar o firefox
option = Options()
option.headless = True
driver = webdriver.Firefox()

driver.get(url)
time.sleep(10)

# Clicar
driver.find.element_by_xpath(
    "//div[@class='nba-stat-table']/table/tread/tr/th[@data-field='PTS']")


driver.quit()
