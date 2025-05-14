# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 12:38:40 2025

@author: levir
"""


# %%
# =============================================================================
# Homework 3 Part 1
# =============================================================================
import pandas as pd
import numpy as np
import os
import requests
  

from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.common.exceptions import NoSuchElementException


options = Options()
options.add_argument("window-size=1400,1200")

driver = webdriver.Chrome(options=options)

url = "https://www.imdb.com/search/title/?genres=family&count=200"

driver.get(url)

try:
    id = driver.find_element(By.ID, "__NEXT_DATA__")
except NoSuchElementException:
    print("Element not found!")
    
try:
    id = driver.find_element(By.CLASS_NAME, "")
except NoSuchElementException:
    print("Element not found!")
driver.find_element(By.NAME, )
driver.find_element(By.TAG_NAME, )
driver.find_element(By.LINK_TEXT, )
driver.find_element(By.PARTIAL_LINK_TEXT, )
driver.find_element(By.X_PATH, )
# %%
# =============================================================================
# Homework 3 Part 2
# =============================================================================
import pandas as pd
import numpy as np

spotify = pd.read_csv('https://bcdanl.github.io/data/spotify_all.csv')
spotify

## Q2
spotify[['artist_name', 'track_name']].value_counts()

## Q3
track_df = spotify[["track_name"]].value_counts()
threshold = track_df.quantile(0.95)
top_5_percent = track_df[track_df > threshold]
top_5_percent

## Q4
spot_1 = spotify.drop_duplicates(subset = ['track_name'])
spot_2 = spot_1[['artist_name']].value_counts()
spot_2.head(75)

## Q5
spotify.query("track_name == 'One Dance'")

## Q6
spotify[["artist_name", "duration_ms"]].max()
spotify[["artist_name", "duration_ms"]].min()

## Q7
spot_3 = spotify[["playlist_name", "track_name"]]
spot_3[spot_3.duplicated()]

## Q8
spot_3 = spot_3.drop_duplicates()
spot_4 = spot_3['track_name'].value_counts()
spot_4.head(13)

# %%
# =============================================================================
# Homework 3 Part 3
# =============================================================================
import pandas as pd
import numpy as np

holiday_movies = pd.read_csv("https://bcdanl.github.io/data/holiday_movies.csv")
df_1 = holiday_movies

holiday_movie_genres = pd.read_csv("https://bcdanl.github.io/data/holiday_movie_genres.csv")
df_2 = holiday_movie_genres

## counting
holiday_movies['title_type'].value_counts()

## filtering
holiday_movies_only_1 = holiday_movies["title_type"] == "movie"
holiday_movies_only = holiday_movies[ holiday_movies_only_1]

good_holiday_movies_only = holiday_movies_only["average_rating"] > 7.5
good_holiday_movies_only = holiday_movies_only[ good_holiday_movies_only ]

good_holiday_movies_only_1 = good_holiday_movies_only["num_votes"] > 100
good_holiday_movies_only_1 = good_holiday_movies_only[ good_holiday_movies_only_1 ]

## sorting
good_holiday_movies_only_1.sort_values(["average_rating"], ascending = False)

## joining
concat = pd.concat([df_1, df_2], axis=1)
concat = concat.dropna()
concat = concat.drop_duplicates()

















