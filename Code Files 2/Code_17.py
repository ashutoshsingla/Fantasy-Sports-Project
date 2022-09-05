#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:53:29 2022

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
diri = "/Users/ashutoshsingla/Desktop/Fantasy_Project/sim_teams1/"

matchdf = pd.read_csv("//Users/ashutoshsingla/Desktop/Fantasy_Project/match_names.csv")   
lsst = matchdf["Match"].tolist()
real_team_length = {}
sim_team_length = {}

for name in lsst:
    print(name)
    df = pd.read_csv(diri+name+".csv")
    sim_team_length[name] = len(df)

                
    
new = pd.DataFrame.from_dict([sim_team_length])
new.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/sim_team_count.csv") 