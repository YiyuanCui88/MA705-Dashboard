#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:52:40 2022

@author: cuiyiyuan
"""

import requests
import pandas as pd

url = "https://realty-mole-property-api.p.rapidapi.com/zipCodes/01605"

headers = {
	"X-RapidAPI-Key": "2328539734msh13f1c6803e8f694p152047jsn1d6b7e25d506",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

Worcester = response.json()
data = Worcester['rentalData']
history = data['history']

frames = []
for date in history.keys():
    d = history[date]
    detail = d['detailed']
    month_df = pd.DataFrame(detail)
    month_df['date'] = date
    frames.append(month_df)
    
    
df = pd.concat(frames)   
df['city'] = "Worcester"
df['zip'] = "01605" 
df['population'] = 27587
df['median household income'] = 42683

df.to_csv("Worcester.csv", index=False)



