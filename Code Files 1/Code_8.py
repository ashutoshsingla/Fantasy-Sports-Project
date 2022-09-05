#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:19:41 2022

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

dir_sim = "/Users/apple/Desktop/projects/Fantasy/simulated_teams/"
dir_p = "/Users/apple/Desktop/projects/Fantasy/conv/"

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()

perm = permutations([0,1,2,3,4,5,6,7,8,9,10], 2)
permlist = list(perm)
mydict = {}
for num in range(0,1):
    name = lsst[num]
    print(name)
    scores=[]
    df_p = pd.read_csv(dir_p+name+'.csv')
    scoredict = {}
    for index, row in df_p.iterrows():
        scoredict[row.iat[2]] = row.iat[5]
        
    df_sim = pd.read_csv(dir_sim+name+'.csv')
    
    for index, row in df_sim.iterrows():
        if(index%10000 == 0):
            print(index)
        thislist = []
        for i in range(1,12):
            #print(str(index)+" "+str(i))
            thislist.append(scoredict[row.iat[i]])
        totscore = sum(thislist)
        for x in permlist:
            #print(totscore+thislist[x[0]]+0.5*thislist[x[1]])
            scores.append(totscore+thislist[x[0]]+0.5*thislist[x[1]])
            #print(str(index)+" "+str(len(scores)))
    
    avg = sum(scores)/len(scores)
    print(avg)
    stddev = statistics.pstdev(scores)
    print(stddev)
    top10 = sum(nlargest(10, scores)) / 10
    top100 = sum(nlargest(100, scores)) / 100
    top1000 = sum(nlargest(1000, scores)) / 1000
    print(top10,top100,top1000)
    mydict[name] = [avg, stddev, top10, top100, top1000]
    # thisdf = pd.DataFrame()
    # thisdf['Score'] = scores
    # thisdf.to_csv('/Users/apple/Desktop/projects/Fantasy/sim_teams1/'+name+'.csv')
#new = pd.DataFrame.from_dict(mydict)
#new.to_csv("/Users/apple/Desktop/projects/Fantasy/sim_match_stats.csv")