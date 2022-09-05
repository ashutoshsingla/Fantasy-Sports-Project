#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 19:05:28 2022

@author: ashutoshsingla
"""

from bs4 import BeautifulSoup
import requests
from itertools import cycle
from itertools import combinations
from itertools import permutations
import random
import pandas as pd
from pprint import pprint
import os
from PyPDF2 import PdfFileReader
from tabula import read_pdf
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import statistics
from heapq import nlargest
import random
from scipy import stats
diri = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files/"
dicti = {}
matchdf = pd.read_csv("//Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")   
lsst = matchdf["Match"].tolist()

for x in range(0, 31):
    name = lsst[x]
    print(name)
    total_df = pd.DataFrame()
    ind = 0
    for subdir, dirs, files in os.walk(diri+name):
        for file in files:
            if file.endswith('.csv'):
                ind+=1
                print(ind)
                df = pd.read_csv(diri+name+"/"+file)              
                total_df = pd.concat([total_df, df], ignore_index=True)
    total_df.drop(df.columns[[0, 1]], axis=1, inplace=True)
    x = len(total_df.drop_duplicates())
    dicti[name] = x
    
new = pd.DataFrame.from_dict([dicti])
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/all_team_count.csv") 