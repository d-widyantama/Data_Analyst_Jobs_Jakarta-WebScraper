# Bot for data Scraping from Indeed.com


# Import Library
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import random

from selenium import webdriver

#Import Packages

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




#Url from LinkedIn 
url = "https://id.linkedin.com/jobs/search?keywords=Data%20Analyst&location=Area%20DKI%20Jakarta&geoId=90010101&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"

#Run the driver and open the url
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)


# # Function for scraping data from Indeed.com
# def extract():
#     headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
#     r = requests.get(url, headers)
#     return r.status_code

# extract()