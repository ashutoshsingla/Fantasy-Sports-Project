#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:25:20 2022

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
dir_c = "/Users/apple/Desktop/projects/Fantasy/Total CSV Scores/"

dir_r = "/Users/apple/Desktop/projects/Fantasy/top_distr/all/"


matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()
bug_dict = []
# for x in range(1,31):
#     name = lsst[x]
#     print(name)
#     mydict = {}
#     num=0
#     df = pd.DataFrame()
#     filelist = []
#     for subdir, dirs, files in os.walk(dir_c+name):
#         for file in files:
#             if file.endswith('.csv'):
#                 filelist.append(file)
#     filelist.sort()
#     for file in filelist:
#         num+=1
#         print(num)
#         df2 = pd.read_csv(dir_c+name+'/'+file)
#         #print("size= "+str(len(df2)))
#         if(num==1):
#             df = df2
#         else:
#             df = df.append(df2, ignore_index=True)
#     for index, row in df.iterrows():
#         if(index%100000 == 0):
#             print(index)
#         nm = row.iat[2]
#         ind = nm.find('(')
#         corrnm = nm[0:ind-1]
#         if(corrnm in mydict):
#             mydict[corrnm].append(row.iat[3])
#         else:
#             mydict[corrnm] = [row.iat[3]]
#     dict_df = pd.DataFrame.from_dict(mydict, orient ='index')
#     dict_df.to_csv('/Users/apple/Desktop/projects/Fantasy/user_dict/all/'+name+'.csv')
#     #mydict = dict
#     tot_dict = {}
#     tot_teams = 0
#     for i in range(1,21):
#         tot_dict[i]=0  
#     for key in mydict:
#         if(len(mydict[key])>20):
#             bug_dict.append([name,key,len(mydict[key])])
#         tot_dict[min(20,len(mydict[key]))] += len(mydict[key])
#         tot_teams += len(mydict[key]) 
         
#     per_tot_dict = {}
#     for key in tot_dict:
#         per_tot_dict[key] = tot_dict[key]*100/tot_teams
#     large50000 = df.nlargest(50000, "Score")
#     per_50000_dict = {}
#     per_5000_dict = {}
#     per_500_dict = {}
#     per_50_dict = {}
#     for kk in range(1,21):
#         per_50000_dict[kk] = 0
#         per_5000_dict[kk] = 0
#         per_500_dict[kk] = 0
#         per_50_dict[kk] = 0
#     mind=0
#     for index, row in large50000.iterrows():
#         mykey = (row.iat[2])[0:row.iat[2].find('(')-1]
#         thisval = min(len(mydict[mykey]),20)
#         per_50000_dict[thisval] += 100/50000
#         if(mind<50):
#             per_50_dict[thisval] += 100/50
#         if(mind<500):
#             per_500_dict[thisval] += 100/500
#         if(mind<5000):
#             per_5000_dict[thisval] += 100/5000
#         mind +=1
#     svdf = pd.DataFrame.from_dict(per_tot_dict, orient ='index')
#     svdf.set_axis(['All Teams (Valid) %'], axis=1, inplace=True)
#     svdf['Top 50k teams %'] = svdf.index.to_series().map(per_50000_dict)
#     svdf['Top 5k teams %'] = svdf.index.to_series().map(per_5000_dict)
#     svdf['Top 500 teams %'] = svdf.index.to_series().map(per_500_dict)
#     svdf['Top 50 teams %'] = svdf.index.to_series().map(per_50_dict)
#     svdf = svdf.round(decimals = 2)
#     svdf.to_csv(dir_r+name+'.csv')
# bug_df = pd.DataFrame(bug_dict)
# bug_df.to_csv('/Users/apple/Desktop/projects/Fantasy/all_bug_users.csv')

all_1 = []
all_2_10 = []
all_11_19 = []
all_20 = []
top_1 = []
top_2_10 = []
top_11_19 = []
top_20 = []
for x in range(0,31):
    name = lsst[x]
    print(name)
    
    df = pd.read_csv('/Users/apple/Desktop/projects/Fantasy/top_distr/all/'+name+'.csv')
    
    var_all_1 = df.iloc[0,1]
    var_all_20 = df.iloc[19,1]
    var_top_1 = df.iloc[0,3]
    var_top_20 = df.iloc[19,3]
    var_all_2_10 = 0
    var_all_11_19 = 0
    var_top_2_10 = 0
    var_top_11_19 = 0
    
    for mynum in range(2,11):
        var_all_2_10 += df.iloc[mynum-1,1]
        var_top_2_10 += df.iloc[mynum-1,3]
    
    for mynum in range(11,20):
        var_all_11_19 += df.iloc[mynum-1,1]
        var_top_11_19 += df.iloc[mynum-1,3]
    
    all_1.append(round(var_all_1,2))
    all_20.append(round(var_all_20,2))
    all_2_10.append(round(var_all_2_10,2))
    all_11_19.append(round(var_all_11_19,2))
    top_1.append(round(var_top_1,2))
    top_20.append(round(var_top_20,2))
    top_2_10.append(round(var_top_2_10,2))
    top_11_19.append(round(var_top_11_19,2))
    


df = pd.DataFrame()
df['Match'] = lsst
df['% of total, 1 team'] = all_1
df['% of total, 2-10 teams'] = all_2_10
df['% of total, 11-19 teams'] = all_11_19
df['% of total, 20 teams'] = all_20
df['% of top 5k, 1 team'] = top_1
df['% of top 5k, 2-10 teams'] = top_2_10
df['% of top 5k, 11-19 teams'] = top_11_19
df['% of top 5k, 20 teams'] = top_20

df.to_csv('/Users/apple/Desktop/projects/Fantasy/top_distr_clubbed_all.csv')
