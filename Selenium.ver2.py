import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# カレントディレクトリの変更
import os
os.chdir(r'D:Selenium')  # ディレクトリを修正

# Seleniumの設定
options = Options()
driver_path = r'D:\hogehoge\chromedriver.exe'  # Chrome Driverのパスを修正
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # ページを開く
    url = 'https://twitter.com/i/flow/login'
    driver.get(url)

    # ログイン情報を入力して次へをクリック
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'))
    )
    username_input.send_keys("@hogehoge")
   
finally:
    close_button = None
