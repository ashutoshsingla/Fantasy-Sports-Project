#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 18:03:11 2022

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
import matplotlib.pyplot as plt
import scipy
from scipy import stats, optimize, interpolate
dir_c = "/Users/ashutoshsingla/Desktop/Fantasy_Project/sim_teams1/24_10_BAN_v_SL.csv"
dir_r = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files1/"
df_c = pd.read_csv(dir_c)
x = df_c['Score'].tolist()
print(sum(x)/len(x))

fig, axs = plt.subplots(1, 1,
                        figsize =(10, 7),
                        tight_layout = True)
axs.hist(x, bins = 100)
plt.show()



matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")    
lsst = matchdf["Match"].tolist()
for name in lsst:
    x = []
    print(name)
    df_c = pd.read_csv(dir_c+name+".csv")
    x = df_c['Score'].tolist()
    fig, axs = plt.subplots(1, 1, figsize =(20, 14), tight_layout = True)
    # x = df_r['Score'].tolist()
    axs.hist(x, range = [0, 1000], bins = 100)
    plt.savefig("/Users/ashutoshsingla/Desktop/Fantasy_Project/Sim_Figures/"+name+".png")
    plt.show()





for name in lsst:
    x = []
    print(name)
    for subdir, dirs, files in os.walk(dir_r+name):
        for file in files:
            if file.endswith('.csv'):
                df = pd.read_csv(dir_r+name+"/"+file)
                x.extend(df['Score'].tolist())
        fig, axs = plt.subplots(1, 1, figsize =(20, 14), tight_layout = True)
        # x = df_r['Score'].tolist()
        axs.hist(x, range = [0, 1000], bins = 100)
        plt.savefig("/Users/ashutoshsingla/Desktop/Fantasy_Project/Real_Figures/"+name+".png")
        plt.show()
        print(sum(x)/len(x))
        
        
        
for name in lsst:
    os.mkdir("/Users/ashutoshsingla/Desktop/Fantasy_Project/Real_Figures/"+name)