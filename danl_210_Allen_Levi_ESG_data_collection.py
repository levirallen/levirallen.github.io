# -*- coding: utf-8 -*-
"""
Created on Sun May 11 17:03:58 2025

@author: levir
"""

# %%
# =============================================================================
# ESG Data
# =============================================================================
import pandas as pd
url_2024 = "https://bcdanl.github.io/data/esg_proj_2024_data.csv"
esg_proj_2024_data = pd.read_csv(url_2024)

url_2025 = "https://bcdanl.github.io/data/esg_proj_2025.csv"
esg_proj_2025 = pd.read_csv(url_2025)

url_yahoo = "https://finance.yahoo.com/"

import time
import random
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


print(os.getcwd())
wd_path = 'C:/Users/levir'
os.chdir(wd_path)

options = Options()
options.add_argument("window-size=1400,1200")
options.add_argument('--disable-blink-features=AutomationControlled')
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(options=options)

merged = pd.merge(esg_proj_2024_data, esg_proj_2025, on='Name')

driver.get(url_yahoo)

url_A_2 = "https://finance.yahoo.com/quote/A/sustainability/"
driver.get(url_A_2)
time.sleep(random.uniform(3, 5))

table_html = driver.find_element(By.TAG_NAME, 'table').get_attribute("outerHTML")
df_A_2 = pd.read_html(StringIO(table_html))[0]

# repeat this process for each company in the merged data frame

driver.quit()





