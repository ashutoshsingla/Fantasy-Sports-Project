#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:55:41 2022

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

mu, sigma = 450, 75
mylist = []
for x in range(50,100):
    print(x)
    s1 = list(np.random.normal(mu, sigma, 4000000))
    s2 = list(np.random.normal(mu, sigma, 4000000))
    
    m1 = sum(s1)/len(s1)
    m2 = sum(s2)/len(s2)
    
    diff = m1-m2
    mylist.append(diff)
    
top10 = nlargest(10, mylist)
