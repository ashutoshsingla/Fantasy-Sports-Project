# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
import numpy as np
dir_ut = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files/"
dir_pp = "/Users/ashutoshsingla/Desktop/Fantasy_Project/conv/"
dir_utnew = "/Users/ashutoshsingla/Desktop/Fantasy_Project/correct_csv_files/"
dir_utnew1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/incorrect_csv_files/"
data_corr = []
data_incorr = []
matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")    
lsst = matchdf["Match"].tolist()
for x in range(8, 9):
    match_name = lsst[x]
    mega_len = 0
    mega_len2 = 0
    print(match_name)
    players = pd.read_csv(dir_pp+match_name+".csv")
    lst = players['CORRECT NAME'].tolist()
    dicti = {}
    for name in lst:
        dicti[name] = 0
    ind = 0
    for subdir, dirs, files in os.walk(dir_ut+match_name):
        for file in files:
            if file.endswith('.csv'):
                ind+=1
                print("CSV "+str(ind))
                user_teams = pd.read_csv(dir_ut+match_name+"/"+file)
                corr = []
                incorr = []
                for index, row in user_teams.iterrows():
                    bl = True
                    for i in range(2, 13):
                        if not row.iat[i] in dicti:
                            bl = False
                            incorr.append(index)
                            break
                    if bl:
                        corr.append(index)
                df_corr = user_teams[user_teams['Unnamed: 0'].isin(corr)]
                df_incorr = user_teams[user_teams['Unnamed: 0'].isin(incorr)]
                df_corr.to_csv(dir_utnew+match_name+"/"+file)
                df_incorr.to_csv(dir_utnew1+match_name+"/"+file)
                mega_len += len(incorr)
                mega_len2 += len(corr)
    data_corr.append((match_name, mega_len2))
    data_incorr.append((match_name, mega_len))
    

# for name in lsst:
#     os.mkdir(dir_utnew1 +name)
    
#     lst_index = []
#     count = 0
#     for index, row in user_teams.iterrows():
#         for i in range(2,13):
#             if not row.iat[i] in dicti:
#                 count+=1
#                 lst_index.append((index, row.iat[i]))
#                 break
#     print(str(x) + "-----" + match_name + "----" + str(len(lst_index)))
#     # for file in files:
#     #     if file.endswith(".csv"):
#     #         bl=False
#     #         break
#     # if


