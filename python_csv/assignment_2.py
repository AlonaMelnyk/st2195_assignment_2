# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:12:25 2023

@author: alion
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/Comma-separated_values"
page=requests.get(url)
soup = BeautifulSoup(page.text,'html')
table= soup.find('table', class_ = 'wikitable')

df_pandas = pd.read_html(url, attrs = {'class': 'wikitable'},  flavor='bs4', thousands ='.')

f = open('assignment2.csv', 'a')
for df in df_pandas:
    df.to_csv(f)
f.close()
