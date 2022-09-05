#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:40:31 2022

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

dir_cut = "/Users/apple/Desktop/projects/Fantasy/correct_csv_files/"
dir_incut = "/Users/apple/Desktop/projects/Fantasy/incorrect_csv_files/"
dir_cut1 = "/Users/apple/Desktop/projects/Fantasy/correct_csv_files1/"
dir_incut1 = "/Users/apple/Desktop/projects/Fantasy/incorrect_csv_files1/"
dir_pp = "/Users/apple/Desktop/projects/Fantasy/conv/"


matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()
score_dict = {}
for name in lsst:
    match_perf_df = pd.read_csv(dir_pp+name+".csv")
    lst = match_perf_df['CORRECT NAME'].tolist()
    lst1 = match_perf_df['FINAL'].tolist()
    dicti = {}
    x=0
    for name1 in lst:
        dicti[name1] = lst1[x]
        x+=1
    main_score_list = []
    for subdir, dirs, files in os.walk(dir_cut+name):
        for file in files:
            if(file.endswith(".csv")):
                score_list = []
                df = pd.read_csv(dir_cut+name+"/"+file)
                for index, row in df.iterrows():
                    score = 0
                    score += 2*dicti[row.iat[3]]
                    score += 1.5*dicti[row.iat[4]]
                    for i in range(5,13):
                        score += dicti[row.iat[i]]
                    score_list.append(score)
                newdf = pd.dataframe
                newdf['User (Team)'] = df['User (Team)']
                newdf['Score'] = score_list
                newdf.to_csv(dir_cut1+name+"/"+file)
                main_score_list = main_score_list + score_list
    
    for subdir, dirs, files in os.walk(dir_incut+name):
        for file in files:
            if(file.endswith(".csv")):
                score_list = []
                df = pd.read_csv(dir_incut+name+"/"+file)
                for index, row in df.iterrows():
                    score = 0
                    if row.iat[3] in dicti:
                        score += 2*dicti[row.iat[3]]
                    if row.iat[4] in dicti:
                        score += 1.5*dicti[row.iat[4]]
                    for i in range(5,13):
                        if row.iat[i] in dicti:
                            score += dicti[row.iat[i]]
                    score_list.append(score)
                newdf = pd.dataframe
                newdf['User (Team)'] = df['User (Team)']
                newdf['Score'] = score_list
                newdf.to_csv(dir_incut1+name+"/"+file)