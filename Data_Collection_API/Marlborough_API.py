#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:31:11 2022

@author: cuiyiyuan
"""

import requests
import pandas as pd

url = "https://realty-mole-property-api.p.rapidapi.com/zipCodes/01752"

headers = {
	"X-RapidAPI-Key": "2328539734msh13f1c6803e8f694p152047jsn1d6b7e25d506",
	"X-RapidAPI-Host": "realty-mole-property-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

marl = response.json()
data = marl['rentalData']
history = data['history']

frames = []
for date in history.keys():
    d = history[date]
    detail = d['detailed']
    month_df = pd.DataFrame(detail)
    month_df['date'] = date
    frames.append(month_df)
    
    
df = pd.concat(frames)   
df['city'] = "Marlborough"
df['zip'] = "01752" 
df['population'] = 39663
df['median household income'] = 83469

df.to_csv("Marlborough.csv", index=False)









    