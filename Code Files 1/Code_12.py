#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 23:20:05 2022

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
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy import stats, optimize, interpolate
import seaborn as sns
dir_c = "/Users/apple/Desktop/projects/Fantasy/sim_teams1/"
dir_r = "//Users/apple/Desktop/projects/Fantasy/correct_csv_files1/"


matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()


for kk in range(0,31):
    name = lsst[kk]
    real = []
    print(name)
    for subdir, dirs, files in os.walk(dir_r+name):
        for file in files:
            if file.endswith('.csv'):
                df = pd.read_csv(dir_r+name+"/"+file)
                real.extend(df['Score'].tolist())
    sim = []
    print("Real score loaded")
    df_c = pd.read_csv(dir_c+name+".csv")
    sim = df_c['Score'].tolist()
    print("Sim score loaded")
    x = np.array(real)
    y = np.array(sim)
    x_w = np.empty(x.shape)
    x_w.fill(1/x.shape[0])
    y_w = np.empty(y.shape)
    y_w.fill(1/y.shape[0])
    # fig, axs = plt.subplots(1, 1, figsize =(20, 14), tight_layout = True)
    # # x = df_r['Score'].tolist()
    # axs.hist(real, range = [0, 1000], bins = 100)
    # axs.hist(sim, range = [0, 1000], bins = 100)
    # p = sns.histplot(data=real, x='Score', stat='Probability', ax=ax)
    # plt.show()
    bins = np.linspace(0, 1000, 100)
    plt.hist(x,bins,weights=x_w,alpha=0.5,label='Real Score')
    plt.hist(y,bins,weights=y_w,alpha=0.5,label='Sim Score')
    #plt.hist([x, y], bins, weights = [x_w, y_w], label=['Real Score', 'Sim Score'])
    plt.legend(loc='upper right')
    plt.savefig("/Users/apple/Desktop/projects/Fantasy/CombinedSimRealHist/"+name+".png")
    plt.show()
        
        
        
for name in lsst:
    os.mkdir("/Users/ashutoshsingla/Desktop/Fantasy_Project/Real_Figures/"+name)