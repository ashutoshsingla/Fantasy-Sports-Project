#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 02:40:59 2022

@author: ashutoshsingla
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

directory = "/Users/ashutoshsingla/Desktop/Fantasy_Project/"
bl=False
for subdir, dirs, files in os.walk(directory+"userteams2"):
    if not bl:
        bl = True
        continue
    
    print(subdir)
    df_tot = pd.DataFrame()
    # if not subdir == "/Users/ashutoshsingla/Desktop/Fantasy_Project/User_Teams/trial":
    #     continue

    for file in files:
        if not file.endswith(".pdf"):
            continue
        print(os.path.join(subdir, file))
        reader = PdfFileReader(open(subdir+"/"+file, 'rb')) 
        cnt = reader.getNumPages()
        x = int((cnt-1)/2500) + 1
        for i in range(1, x+1):
            start = 2500*(i-1) + 1
            end = min(2500*i, cnt)
            df = read_pdf(subdir+"/"+file,pages=str(start)+"-"+str(end)) #address of pdf file
            if df[0].loc[0][0] == 'User (Team)':    
                new_header = df[0].iloc[0] #grab the first row for the header
                df[0] = df[0][1:] #take the data less the header row
                df[0].columns = new_header #set the header row as the df header
            df2 = pd.concat([df2, df], ignore_index=True)
            for j in range(len(df2)):
                df2.loc[j].iat[0] = df2.loc[j].iat[0].replace("\r"," ")
            match_name = subdir[57:]
            df2.to_csv(directory+"csv_files/" +match_name+"/"+file[:-4]+"_Part"+str(i)+".csv", index=True)
            
            
            


    
