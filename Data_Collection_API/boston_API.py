#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:44:23 2022

@author: cuiyiyuan
"""

import requests
import pandas as pd

url = "https://realty-mole-property-api.p.rapidapi.com/zipCodes/02128"

headers = {
	"X-RapidAPI-Key": "2328539734msh13f1c6803e8f694p152047jsn1d6b7e25d506",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

boston = response.json()
#dict_keys(['id', 'rentalData'])
#boston['id']
data = boston['rentalData']
#dict_keys(['averageRent', 'minRent', 'maxRent', 'totalRentals', 'detailed', 'history'])
history = data['history']

frames = []
for date in history.keys():
    d = history[date]
    detail = d['detailed']
    month_df = pd.DataFrame(detail)
    month_df['date'] = date
    frames.append(month_df)
    
    
df = pd.concat(frames)    

df['city'] = "Boston"
df['zip'] = "02128"
df['population'] = 47804
df['median household income'] = 63378

df.to_csv("Boston.csv", index=False)
    
    
#Apr = history['2020-04']    
#detail = Apr['detailed']











