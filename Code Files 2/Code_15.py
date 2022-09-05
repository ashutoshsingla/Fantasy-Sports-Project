

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

dir = "/Users/ashutoshsingla/Desktop/Fantasy_Project/"

matchdf = pd.read_csv("//Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")   
lsst = matchdf["Match"].tolist()
dict_win_real = {}

binss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in range(0, 31):
    name = lsst[x]
    print(name)
    df_sim = pd.read_csv(dir+'sim_teams1/'+name+'.csv')
    sim_score = df_sim['Score'].tolist()
    real_score = []
    for subdir, dirs, files in os.walk(dir+'csv_files1/'+name+'/'):
        for file in files:
            if(file.endswith(".csv")):
                df_temp = pd.read_csv(dir+'csv_files1/'+name+'/'+file)
                real_score.extend(df_temp['Score'].tolist())
    lst_score = []
    for i in range(0,len(real_score)):
        thisscore = 0
        a = real_score[i]
        for j in range(0, 10):
            b = random.choice(sim_score)
            if a>=b:
                thisscore += 1
        lst_score.append(thisscore)
        if(len(lst_score)%1000000 == 0):
            print(len(lst_score))
    dict_win_real[name] = [sum(lst_score)/len(lst_score), statistics.pstdev(lst_score)]
  
    data = np.array(lst_score)  
    d = np.diff(np.unique(data)).min() 
    plt.margins(0)
    left_of_first_bin = data.min() - float(d)/2 
    right_of_last_bin = data.max() + float(d)/2 
    plt.hist(data, np.arange(left_of_first_bin, right_of_last_bin + d, d)) 
    plt.xlabel('Score out of 10')
    plt.xticks(binss)
    plt.ylabel('Frequency')
    plt.savefig(dir + 'one_on_ten_fig_newer/all/' +lsst[x]+'.png', bbox_inches='tight')
    plt.show()
    
    
new = pd.DataFrame.from_dict(dict_win_real)
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/simulation3all.csv") 