#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 23:53:01 2022

@author: ashutoshsingla
"""

from bs4 import BeautifulSoup
import requests
from itertools import cycle
from itertools import combinations
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

dir_ppmod1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/conv2/"
# dir_ppmod2 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/sim_score/"

lsst = lsst[8:9]

for name in lsst:
    match_perf_df = pd.read_csv(dir_pp+name+".csv")
    print(name)
    dict_score = {}
    dict_credit = {}
    dict_p = {}
    lst = match_perf_df['CORRECT NAME'].tolist()
    for name2 in lst:
        dict_p[name2] = 0

    for index, row in match_perf_df.iterrows():
        dict_score[row.iat[2]] = row.iat[5]
        dict_credit[row.iat[2]] = row.iat[4]
    ind = 0
    file = dir_cut+name+".csv"
    df = pd.read_csv(file)
    cnt = len(df)
    # scores = []
    # credits = []
    for index, row in df.iterrows():
        # thisscore = 0
        # thiscredit = 0
        for i in range(1,12):
            dict_p[row.iat[i]]+=1
            # thisscore += dict_score[row.iat[i]]
            # thiscredit += dict_credit[row.iat[i]]
        # credits.append(thiscredit)
        # scores.append(thisscore)
    match_perf_df['Captain'] = match_perf_df['CORRECT NAME'].map(dict_p)
    match_perf_df['Vice Captain'] = match_perf_df['CORRECT NAME'].map(dict_p)
    match_perf_df['Chosen'] = 110*match_perf_df['CORRECT NAME'].map(dict_p)
    match_perf_df['Total Teams'] = pd.Series([cnt for x in range(len(match_perf_df))])
    match_perf_df.to_csv(dir_ppmod1+name+".csv")
    # score_df = pd.DataFrame()
    # score_df['Credits'] = credits
    # score_df['Scores'] = scores
    # score_df.to_csv(dir_ppmod2+name+".csv")
    break