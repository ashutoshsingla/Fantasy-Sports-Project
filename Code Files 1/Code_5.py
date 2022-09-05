#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 23:40:19 2022

@author: apple
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

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()

# for name in lsst:
#     os.mkdir('/Users/apple/Desktop/projects/Fantasy/simulated_teams/'+name)
my_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
column_names = []
for i in range(1,12):
    column_names.append('Player '+str(i))
for x in range(14,31):
    name = lsst[x]
    print(name)
    sim_teams = pd.DataFrame(columns = column_names)
    df = pd.read_csv('/Users/apple/Desktop/projects/Fantasy/conv/'+name+'.csv')
    tot_list = list(combinations(my_list, 11))
    tma = df['CTY'][0]
    for this_list in tot_list:
        num_tma=0
        num_bat=0
        num_wk=0
        num_ar=0
        num_bowl=0
        num_cred=0
        for ply in this_list:
            if df['CTY'][ply]==tma:
                num_tma+=1
            if df['TYPE'][ply]=='WK':
                num_wk+=1
            elif df['TYPE'][ply]=='BAT':
                num_bat+=1
            elif (df['TYPE'][ply]=='ALL' or df['TYPE'][ply]=='AR'):
                num_ar+=1
            else:
                num_bowl+=1
            num_cred += df['CREDITS'][ply]
        if (num_tma>=4 and num_tma<=7 and num_bat>=3 and num_bat<=6 and num_wk>=1 and num_wk<=4 and num_ar>=1 and num_ar<=4 and num_bowl>=3 and num_bowl<=6 and num_cred <=100):
            this_list_name = []
            for ind in this_list:
                this_list_name.append(df['CORRECT NAME'][ind])
            sim_teams.loc[len(sim_teams)] = this_list_name
    sim_teams.to_csv('/Users/apple/Desktop/projects/Fantasy/simulated_teams/'+name+'.csv')