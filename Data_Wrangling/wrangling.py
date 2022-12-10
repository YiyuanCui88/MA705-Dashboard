#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:25:42 2022

@author: cuiyiyuan
"""

import pandas as pd
import numpy as np
import os
import glob

#list all csv files only
csv_files = glob.glob('*.{}'.format('csv'))

city_frames = []
#append all files together
for file in csv_files:
    df_temp = pd.read_csv(file)
    city_frames.append(df_temp)
    
df = pd.concat(city_frames)  
col = {t:t.strip().title() for t in df.columns}
df.rename(columns = col, inplace=True)
df.rename(columns={'Averagerent': 'Avg_Rent', 'Minrent': 'Min_Rent', 'Maxrent':'Max_Rent', 'Totalrentals':'Total Rentals'}, inplace=True)
df['Zip'] = df.Zip.astype(str).str.zfill(5)
df['City_Zip'] = df[['City','Zip']].agg('_'.join, axis=1)
df = df[df.Bedrooms<=5]

#df.to_csv('All_data.csv', index=False)
#df.to_excel('All_data.xlsx', index=False)

#df.to_excel('Master File.xlsx', index=False)






    

