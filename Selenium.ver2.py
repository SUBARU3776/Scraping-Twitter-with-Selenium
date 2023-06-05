import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Change of current directory
import os
os.chdir(r'D:Selenium')  # Fix directory

# Selenium Configuration
options = Options()
driver_path = r'D:\hogehoge\chromedriver.exe'  # Fix Chrome Driver paths
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open page
    url = 'https://twitter.com/i/flow/login'
    driver.get(url)

    # Enter your login information
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
    )
    username_input.send_keys("@hogehoge")
   
finally:
    close_button = None
