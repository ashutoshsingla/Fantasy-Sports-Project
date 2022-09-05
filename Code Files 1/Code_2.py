#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 14:19:15 2022

@author: ashutoshsingla
"""

from bs4 import BeautifulSoup
import requests
from itertools import cycle
import random
import pandas as pd
from pprint import pprint
import os
from PyPDF2 import PdfFileReader
from tabula import read_pdf
from tabulate import tabulate

directory = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files/N14_11_AUS_v_NZ/"
user_teams = pd.read_csv(directory+"AUSvsNZ-19l31i5eep183--1-3786717215_Part1.csv")
players = pd.read_csv(directory+"N14_11_AUS_v_NZ - Sheet1.csv")

lst = players['CORRECT NAME'].tolist()
dicti = {}
for name in lst:
    dicti[name] = [0, 0, 0]
# dicti = dict.fromkeys(lst, [0, 0, 0])

for index, row in user_teams.iterrows():
    for i in range(2,13):
        if row.iat[i] in dicti:
            if i==2:
                dicti[row.iat[i]][0]+=1
                dicti[row.iat[i]][2]+=1
            elif i==3:
                dicti[row.iat[i]][1]+=1
                dicti[row.iat[i]][2]+=1
            else:
                dicti[row.iat[i]][2]+=1
                
myInt = user_teams.shape[0]
dictp = {}
for key in dicti:
    dictp[key] = [x*100 / myInt  for x in dicti[key]]
    
#code for calculating part 2
lst_index = []
count = 0
for index, row in user_teams.iterrows():
    for i in range(2,13):
        if not row.iat[i] in dicti:
            count+=1
            lst_index.append((index, row.iat[i]))
            break
            
            



# lst2 = list(user_teams)
# lst2 = lst2[2:]
# for row in user_teams:
#     for x in lst2:
        
#         # x = row.player1(captain)
#         # players.x.captain++
#         # players.x.include++
        




