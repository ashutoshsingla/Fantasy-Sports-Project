#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:07:23 2022

@author: apple
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
matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")    
lsst = matchdf["Match"].tolist()
dir_cut = "/Users/ashutoshsingla/Desktop/Fantasy_Project/correct_csv_files/"
dir_pp = "/Users/ashutoshsingla/Desktop/Fantasy_Project/conv/"
dir_ppmod = "/Users/ashutoshsingla/Desktop/Fantasy_Project/Total Match Stats/"
diri = "/Users/ashutoshsingla/Desktop/Fantasy_Project/incorrect_csv_files/"
lsst = lsst[8:9]


for name in lsst:
    # match_perf_df = pd.read_csv(dir_pp+name+".csv")
    print(name)
    dict_p = {}
    dict_c = {}
    dict_vc = {}
    lst = match_perf_df['CORRECT NAME'].tolist()
    for name2 in lst:
        dict_p[name2] = 0
        dict_c[name2] = 0
        dict_vc[name2] = 0
    cnt=0
    ind = 0
    for subdir, dirs, files in os.walk(diri+name):
        for file in files:
            if file.endswith('.csv'):
                ind+=1
                print("CSV "+str(ind))
                df = pd.read_csv(diri+name+"/"+file)
                cnt += len(df)
                for index, row in df.iterrows():
                    if row.iat[3] in dict_p:
                        dict_c[row.iat[3]]+=1
                    if row.iat[4] in dict_p:
                        dict_vc[row.iat[4]]+=1
                    for i in range(3,13):
                        if row.iat[i] in dict_p:
                            dict_p[row.iat[i]]+=1
                            
                            
    match_perf_df['Captain'] = match_perf_df['CORRECT NAME'].map(dict_c)
    match_perf_df['Vice Captain'] = match_perf_df['CORRECT NAME'].map(dict_vc)
    match_perf_df['Chosen'] = match_perf_df['CORRECT NAME'].map(dict_p) 
    match_perf_df['Total Teams'] = pd.Series([cnt for x in range(len(match_perf_df))])
                      
    match_perf_df['IN_Captain'] = match_perf_df['CORRECT NAME'].map(dict_c)
    match_perf_df['IN_Vice Captain'] = match_perf_df['CORRECT NAME'].map(dict_vc)
    match_perf_df['IN_Chosen'] = match_perf_df['CORRECT NAME'].map(dict_p)
    match_perf_df['IN_Total Teams'] = pd.Series([cnt for x in range(len(match_perf_df))])
    match_perf_df['All_Captain'] = match_perf_df['Captain'] + match_perf_df['IN_Captain']
    match_perf_df['All_Vice_Captain'] = match_perf_df['Vice Captain'] + match_perf_df['IN_Vice Captain']
    match_perf_df['All_Chosen'] = match_perf_df['Chosen'] + match_perf_df['IN_Chosen']
    match_perf_df['All_Total_Teams'] = match_perf_df['Total Teams'] + match_perf_df['IN_Total Teams']

    match_perf_df.to_csv(dir_ppmod+name+".csv")
    
 