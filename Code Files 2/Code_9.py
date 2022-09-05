#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 15:24:04 2022

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
matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")    
lsst = matchdf["Match"].tolist()
dir1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/correct_csv_files1/"
dir2 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/incorrect_csv_files1/"
dir3 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files1/"
for name in lsst:
    correct_list = []
    incorrect_list = []
    print(name)
    for subdir, dirs, files in os.walk(dir1+name):
        for file in files:
            if file.endswith('.csv'):
                correct_list.append(file)
    for subdir, dirs, files in os.walk(dir2+name):
        for file in files:
            if file.endswith('.csv'):
                incorrect_list.append(file)
    correct_list.sort()
    incorrect_list.sort()
    for x in range(0, len(correct_list)):
        df_c = pd.read_csv(dir1+name+"/"+correct_list[x])
        df_i = pd.read_csv(dir2+name+"/"+incorrect_list[x])
        df_c['isCorrect'] = pd.Series(1 for x in range(len(df_c)))
        df_i['isCorrect'] = pd.Series(0 for x in range(len(df_i)))
        df_total = pd.concat([df_c, df_i])
        df_total.to_csv(dir3+name+"/"+correct_list[x])

for name in lsst:
    os.mkdir("/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files1/"+name)