#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:01:36 2022

@author: ashutoshsingla
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 23:53:01 2022

@author: ashutoshsingla
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

matchdf = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")   
lsst = matchdf["Match"].tolist()
dir_cut = "/Users/ashutoshsingla/Desktop/Fantasy_Project/csv_files/"
dir_cut1 = "/Users/ashutoshsingla/Desktop/Fantasy_Project/Count/"
for name in lsst:
    print(name)
    dict_p = {}
    dict_c = {}
    dict_vc = {}
    ind = 0
    cnt = 0
    for subdir, dirs, files in os.walk(dir_cut+name+'/'):
        for file in files:
            if(file.endswith(".csv")):
                ind+=1
                print(ind)
                df = pd.read_csv(dir_cut+name+'/'+file)
                cnt += len(df)
                for index, row in df.iterrows():
                    if row.iat[2] in dict_c:
                        dict_c[row.iat[2]]+=1
                    else:
                        dict_c[row.iat[2]] = 1
                    if row.iat[3] in dict_vc:
                        dict_vc[row.iat[3]]+=1
                    else:
                        dict_vc[row.iat[3]]=1
                    for i in range(2,13):
                        if row.iat[i] in dict_p:
                            dict_p[row.iat[i]]+=1
                        else:
                            dict_p[row.iat[i]] = 1

    match_perf_df = pd.DataFrame(list(dict_p.items()), columns=['CORRECT NAME', 'Chosen'])
    match_perf_df['Captain'] = match_perf_df['CORRECT NAME'].map(dict_c)
    match_perf_df['Vice Captain'] = match_perf_df['CORRECT NAME'].map(dict_vc)
    match_perf_df['Total Teams'] = pd.Series([cnt for x in range(len(match_perf_df))])
    match_perf_df.to_csv(dir_cut1+name+".csv")
  
    

for name in lsst:
    os.mkdir("/Users/ashutoshsingla/Desktop/Fantasy_Project/Count/"+name)