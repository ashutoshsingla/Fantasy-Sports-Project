#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:58:09 2022

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
diri = "/Users/ashutoshsingla/Desktop/Fantasy_Project/"

matchdf = pd.read_csv("//Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")   
lsst = matchdf["Match"].tolist()
dicti2 = {}

for x in range(0, 31):
    name = lsst[x]
    print(name)
    df = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/user_dict_all/" + name+".csv")
    dicti = df.set_index('Unnamed: 0').T.to_dict('list')  
    for key, value in dicti.items():
        ind = 20
        for ele in range(0, len(value)):
            if str(value[ele]) == 'nan':
                ind = ele 
                break
        dicti[key] = value[0:ind]
    one_list = []
    multiple_list = []
    for key, value in dicti.items():
        if len(value)>1:
            multiple_list.extend(value)
        else:
            one_list.extend(value)
    t_value,p_value = stats.ttest_ind(one_list, multiple_list)
    alpha = 0.05
    if p_value<=alpha:
        dicti2[name] = (sum(one_list)/len(one_list), sum(multiple_list)/len(multiple_list), t_value, p_value, "Rejected")
        #print("We reject the null hypothesis")
    else:
        dicti2[name] = (sum(one_list)/len(one_list), sum(multiple_list)/len(multiple_list), t_value, p_value, "Accepted")

    x = np.array(one_list)
    y = np.array(multiple_list)
    x_w = np.empty(x.shape)
    x_w.fill(1/x.shape[0])
    y_w = np.empty(y.shape)
    y_w.fill(1/y.shape[0])
    bins = np.linspace(0, 1000, 100)
    plt.hist(x,bins,weights=x_w,alpha=0.5,label='Single Team Score')
    plt.hist(y,bins,weights=y_w,alpha=0.5,label='Multiple Team Score')
    plt.legend(loc='upper right')
    plt.savefig("/Users/ashutoshsingla/Desktop/Fantasy_Project/Single_v_Multiple_all/"+name+".png")
    plt.show()
    
    
    
new = pd.DataFrame.from_dict(dicti2)
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/SingleVsMultiple_all.csv") 
    
    
    
        

            

    
    