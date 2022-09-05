#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 18:51:06 2022

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
from scipy import stats

# a = [13.4,10.9,11.2,11.8,14,15.3,14.2,12.6,17,16.2,16.5,15.7]
# c = [13.4,10.9,11.2,11.8,14,15.3,14.2,12.6,17,16.2,16.5,15.7]
# b = [12,11.7,10.7,11.2,14.8,14.4,13.9,13.7,16.9,16,15.6,16]
# t_value,p_value=stats.ttest_ind(a,c)
# alpha = 0.05

# if p_value<=alpha:

#     print('Conclusion','n','Since p-value(=%f)'%p_value,'<','alpha(=%.2f)'%alpha,'''We reject the null hypothesis H0. So we conclude that the 

# effect of ammonium chloride and urea on grain yield of paddy are not equal i.e., μ1 = μ2 at %.2f level of significance.'''%alpha)

# else:

#     print('Conclusion','n','Since p-value(=%f)'%p_value,'>','alpha(=%.2f)'%alpha,'''We do not reject the null hypothesis H0.
# So we conclude that the effect of ammonium chloride and urea on grain yield of paddy are equal
# i.e., μ1 ≠ μ2 at %.2f level of significance.'''%alpha)


dir = "/Users/apple/Desktop/projects/Fantasy/"

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()
dict_win_real = {}

df = pd.DataFrame(columns=['Match','t-value','p-value','Null Hypothesis'])
for x in range(1,31):
    name = lsst[x]
    print(name)
    df_sim = pd.read_csv(dir+'sim_teams1/'+name+'.csv')
    sim_score = df_sim['Score'].tolist()
    real_score = []
    ind=0
    for subdir, dirs, files in os.walk(dir+'Total CSV Scores/'+name+'/'):
        for file in files:
            if(file.endswith(".csv")):
                ind+=1
                print(ind)
                df_temp = pd.read_csv(dir+'Total CSV Scores/'+name+'/'+file)
                real_score.extend(df_temp['Score'].tolist())
    sim_score_reduced = random.sample(sim_score, len(real_score))
    t_value,p_value=stats.ttest_ind(real_score,sim_score_reduced)
    alpha = 0.05
    if p_value<=alpha:
        df.loc[len(df)] = [name,t_value,p_value,'Rejected'] 
        #print("We reject the null hypothesis")
    else:
        df.loc[len(df)] = [name,t_value,p_value,'Accepted'] 
        #print("We accept the null hypothesis")
    
df.to_csv(dir+'t_stats_realSim_sameSize.csv')
