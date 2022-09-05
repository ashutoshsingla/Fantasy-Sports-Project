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

dir_cut = "/Users/apple/Desktop/projects/Fantasy/correct_csv_files/"
dir_pp = "xyz/"
dir_ppmod = "abc/"

lsst = []

for name in lsst:
    match_perf_df = pd.read_csv(dir_pp+name)
    dict_p = {}
    dict_c = {}
    dict_vc = {}
    cnt=0
    for subdir, dirs, files in os.walk(dir_cut+name):
        for file in files:
            if file.endswith('.csv'):
                df = pd.read_csv(dir_cut+name+"/"+file)
                cnt += len(df)
                for row, index in df.iterrows():
                    dict_c[row.iat[3]]+=1
                    dict_vc[row.iat[4]]+=1
                    for i in range(3,13):
                        dict_p[row.iat[i]]+=1
    match_perf_df['Captain'] = match_perf_df['CORRECT NAME'].map(dict_c)
    match_perf_df['Vice Captain'] = match_perf_df['CORRECT NAME'].map(dict_vc)
    match_perf_df['Chosen'] = match_perf_df['CORRECT NAME'].map(dict_p)
    match_perf_df['Total Teams'] = pd.Series([cnt for x in range(len(match_perf_df))])
    match_perf_df.to_csv(dir_ppmod+name+".csv")
    
    