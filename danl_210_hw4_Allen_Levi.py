# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 09:13:59 2025

@author: levir
"""

# %%
# =============================================================================
# Homework 4 Part 1
# =============================================================================

from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
import numpy as np
import os
import requests

options = Options()
options.add_argument("window-size=1400,1200")

driver = webdriver.Chrome(options=options)

url = "https://www.nyc.gov/site/finance/property/property-annualized-sales-update.page"
driver.get(url)

## Question 1
download_link_1 = "https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/neighborhood_sales/2024/2024_manhattan.xlsx"
download_link_2 = "https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/neighborhood_sales/2024/2024_bronx.xlsx"
download_link_3 = "https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/neighborhood_sales/2024/2024_brooklyn.xlsx"
download_link_4 = "https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/neighborhood_sales/2024/2024_queens.xlsx"
download_link_5 = "https://www.nyc.gov/assets/finance/downloads/pdf/rolling_sales/neighborhood_sales/2024/2024_statenisland.xlsx"

# Question 2
url_2 = "https://bcdanl.github.io/data/fred_api_series_housing_price.csv"
driver.get(url_2)
series_housing_price = pd.read_csv(url_2)




# %%
# =============================================================================
# Homework 3 Part 2
# =============================================================================
import pandas as pd
import numpy as np

cms_ny_2022 = pd.read_csv('https://bcdanl.github.io/data/cms-2022-cities-all.zip')

## Question 3
cms_ny_2022["Physician_or_NPP"] = cms_ny_2022["Physician_or_NPP"].astype("category")

## Question 5
cms_ny_2022_AoP = cms_ny_2022["Amount_of_Payment"]
threshold = cms_ny_2022_AoP.quantile(0.90)
top_10_percent = cms_ny_2022_AoP[cms_ny_2022_AoP > threshold]
top_10_percent

## Question 7
cms_ny_2022_df1 = cms_ny_2022[['Taxonomy', 'Specialty_Detail']].value_counts()
cms_ny_2022_df1["Allopathic & Osteopathic Physicians"]
cms_ny_2022_df1["Physician Assistants & Advanced Practice Nursing Providers"]
cms_ny_2022_df1["Dental Providers"]
cms_ny_2022_df1["Nursing Service Providers"]
cms_ny_2022_df1["Eye and Vision Services Providers"]
cms_ny_2022_df1["Chiropractic Providers"]
cms_ny_2022_df1["Podiatric Medicine & Surgery Service Providers"]

## Question 8
dentist = cms_ny_2022_df1["Dental Providers"]
dentist.nunique()

## Question 9
cms_ny_2022.isna().sum()

dermatology = cms_ny_2022["Specialty"] == "Dermatology"
dermatology = cms_ny_2022[dermatology]
dermatology['Amount_of_Payment'].describe()

## Question 10
city_info = cms_ny_2022[['City', 'Physician_or_NPP']]
city_info = city_info.groupby(['City', 'Physician_or_NPP']).value_counts()
city_info = city_info.reset_index()
city_info

## Question 11
roc = cms_ny_2022["City"] == "Rochester"
buff = cms_ny_2022["City"] == "Buffalo"
syr = cms_ny_2022["City"] == "Syracuse"
rbs_df = cms_ny_2022[ roc|buff|syr ]

rbs_df1 = rbs_df["Product_Manufacturer"] == "AbbVie Inc."
rbs_df1 = rbs_df[rbs_df1]
rbs_df1['Amount_of_Payment'].sum() # 117565.31

rbs_df1["Product_Manufacturer"].value_counts() # 5633

## Question 12
cms_ny_2022_npi = pd.read_csv('https://bcdanl.github.io/data/cms-2022-cities-npi.csv')
cms_ny_2022_records = pd.read_csv('https://bcdanl.github.io/data/cms-2022-cities-records.csv')

cms_ny_2022_1 = pd.concat([cms_ny_2022_records, cms_ny_2022_npi], axis=1)
cms_ny_2022_1

## Question 13
city_info_2 = cms_ny_2022[['City', 'Physician_or_NPP']]
Physician = city_info_2["Physician_or_NPP"] == "Physician"
NPP = city_info_2["Physician_or_NPP"] == "NPP"
Physician = city_info_2[Physician]
NPP = city_info_2[NPP]

Physician = Physician.rename( columns= {"Physician_or_NPP":"Physician"})
NPP = NPP.rename( columns= {"Physician_or_NPP":"NPP"})

Phys_NPP = pd.concat([Physician, NPP], axis=1)
Phys_NPP




















