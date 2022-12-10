#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:38:45 2022

@author: cuiyiyuan
"""

import requests
import pandas as pd

url = "https://realty-mole-property-api.p.rapidapi.com/zipCodes/02452"

headers = {
	"X-RapidAPI-Key": "2328539734msh13f1c6803e8f694p152047jsn1d6b7e25d506",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

waltham = response.json()
data = waltham['rentalData']
history = data['history']

frames = []
for date in history.keys():
    d = history[date]
    detail = d['detailed']
    month_df = pd.DataFrame(detail)
    month_df['date'] = date
    frames.append(month_df)
    
    
df = pd.concat(frames)   
df['city'] = "Waltham"
df['zip'] = "02452"
df['population'] = 15636
df['median household income'] = 99747
 

df.to_csv("Waltham.csv", index=False)








