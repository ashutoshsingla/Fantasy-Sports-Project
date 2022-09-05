#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 22:45:56 2022

@author: apple
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

dir = "/Users/apple/Desktop/projects/Fantasy/"

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()
dict_win_real = {}


for x in range(1,31):
    name = lsst[x]
    df_sim = pd.read_csv(dir+'sim_teams1/'+name+'.csv')
    sim_score = df_sim['Score'].tolist()
    real_score = []
    for subdir, dirs, files in os.walk(dir+'correct_csv_files1/'+name+'/'):
        for file in files:
            if(file.endswith(".csv")):
                df_temp = pd.read_csv(dir+'correct_csv_files1/'+name+'/'+file)
                real_score.extend(df_temp['Score'].tolist())
    diff_score = []
    win_real = 0
    win_sim = 0
    tie = 0
    for i in range(0,1000000):
        a = random.choice(real_score)
        b = random.choice(sim_score)
        diff_score.append(a-b)
        if a>b:
            win_real += 1
        elif b>a:
            win_sim += 1
        else:
            tie += 1
    dict_win_real[name] = [win_real/1000000, sum(diff_score)/len(diff_score),statistics.pstdev(diff_score)]
    n, bins, patches = plt.hist(diff_score, 100, density=True, facecolor='g', alpha=0.75)
    plt.xlabel('Diff')
    plt.ylabel('Probability')
    plt.title('Histogram of real - sim score')
    #plt.text(400, .045, "Win(real)% = "+str(round(dict_win_real[name],2)))
    plt.xlim(-600, 600)
    #plt.ylim(0, 0.03)
    plt.grid(True)
    plt.savefig(dir+'one_on_one_fig/valid/'+name+'.png')
    plt.show()

new = pd.DataFrame.from_dict(dict_win_real)
new.to_csv("/Users/apple/Desktop/projects/Fantasy/one_on_one_valid_match.csv")