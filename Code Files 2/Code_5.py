#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 18:22:58 2022

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
import statistics
from heapq import nlargest



dir_cut = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files/"
dir_incut = "/Users/ashutoshsingla/Desktop/Fantasy_Project/incorrect_csv_files/"
dir_cut1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/correct_csv_files1/"
dir_incut1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/incorrect_csv_files1/"
dir_pp = "/Users/ashutoshsingla/Desktop/Fantasy_Project/conv/"


matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")    
lsst = matchdf["Match"].tolist()
score_dict = {}
# lsst = lsst[8:9]
for name in lsst:
    print(name)
    match_perf_df = pd.read_csv(dir_pp+name+".csv")
    lst = match_perf_df['CORRECT NAME'].tolist()
    lst1 = match_perf_df['FINAL'].tolist()
    dicti = {}
    x=0
    for name1 in lst:
        dicti[name1] = lst1[x]
        x+=1
    main_score_list = []
    ind = 0
    for subdir, dirs, files in os.walk(dir_cut+name):
        for file in files:
            if(file.endswith(".csv")):
                ind+=1
                print("CSV "+str(ind))
                score_list = []
                df = pd.read_csv(dir_cut+name+"/"+file)
                for index, row in df.iterrows():
                    score = 0
                    score += 2*dicti[row.iat[3]]
                    score += 1.5*dicti[row.iat[4]]
                    for i in range(5,13):
                        score += dicti[row.iat[i]]
                    score_list.append(score)
                newdf = pd.DataFrame()
                newdf['User (Team)'] = df['User (Team)']
                newdf['Score'] = score_list
                newdf.to_csv(dir_cut1+name+"/"+file)
                main_score_list = main_score_list + score_list
    avg = sum(main_score_list)/len(main_score_list)
    stddev = statistics.pstdev(main_score_list)
    top10 = sum(nlargest(10, main_score_list)) / 10
    top100 = sum(nlargest(100, main_score_list)) / 100
    top1000 = sum(nlargest(1000, main_score_list)) / 1000
    score_dict[name] = [avg, stddev, top10, top100, top1000]
    
    # ind2 = 0
    # for subdir, dirs, files in os.walk(dir_incut+name):
    #     for file in files:
    #         if(file.endswith(".csv")):
    #             ind2+=1
    #             print("Incorrect CSV "+str(ind2))
    #             score_list = []
    #             df = pd.read_csv(dir_incut+name+"/"+file)
    #             for index, row in df.iterrows():
    #                 score = 0
    #                 if row.iat[3] in dicti:
    #                     score += 2*dicti[row.iat[3]]
    #                 if row.iat[4] in dicti:
    #                     score += 1.5*dicti[row.iat[4]]
    #                 for i in range(5,13):
    #                     if row.iat[i] in dicti:
    #                         score += dicti[row.iat[i]]
    #                 score_list.append(score)
    #             newdf = pd.DataFrame()
    #             newdf['User (Team)'] = df['User (Team)']
    #             newdf['Score'] = score_list
    #             newdf.to_csv(dir_incut1+name+"/"+file)
                
new = pd.DataFrame.from_dict(score_dict)
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/valid_match_stats.csv")


med_lst = []
# score_dict = {}
dir_cuti = "/Users/ashutoshsingla/Desktop/Fantasy_Project/sim_teams1/"

for name in lsst:
    lst = []
    print(name)
    for subdir, dirs, files in os.walk(dir_cuti):
        for file in files:
            if(file.endswith(".csv")):
                df = pd.read_csv(dir_cuti+"/"+file)
                lst.extend(df['Score'].to_list())
    lst.sort()
    print("done!")
    # medians = statistics.median(lst)
    # med_lst.append(medians)
    # avg = sum(lst)/len(lst)
    # stddev = statistics.pstdev(lst)
    # top10 = sum(nlargest(10, lst)) / 10
    # top100 = sum(nlargest(100, lst)) / 100
    # top1000 = sum(nlargest(1000, lst)) / 1000
    # score_dict[name] = [avg, stddev, top10, top100, top1000]


matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/summary/sim_match_stats.csv") 
matchdf['Median'] = med_lst
matchdf.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/newsummary/sim_match_stats.csv")

      
new = pd.DataFrame.from_dict(score_dict)
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/newsummary/all_match_stats.csv")

    
# for name in lsst:
#     os.mkdir(dir_cut1+name)
#     os.mkdir(dir_incut1+name)

# res = sum(nlargest(3, [5, 4, 3, 2, 1]))