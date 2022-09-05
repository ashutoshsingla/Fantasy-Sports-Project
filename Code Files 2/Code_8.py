#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 00:08:26 2022

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
diri = "/Users/ashutoshsingla/Desktop/Fantasy_Project/Total Match Stats/"
new_df = pd.DataFrame(columns = ['Match', '% Invalid Teams'])
lst = []
for name in lsst:
    df = pd.read_csv(diri+name+".csv")
    lst.append((df.iloc[0]['All_Total_Teams'] - df.iloc[0]['Total Teams']) / df.iloc[0]['All_Total_Teams'])
multiplied_list = [element * 100 for element in lst]

new_df['Match'] = lsst
new_df['% Invalid Teams'] = multiplied_list

new_df.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/Percent_Invalid_Teams.csv")
