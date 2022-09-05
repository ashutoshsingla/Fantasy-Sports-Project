#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:44:46 2022

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
import statistics
from scipy.stats import mannwhitneyu
from scipy.stats import wilcoxon
from scipy.stats import kruskal
from scipy.stats import friedmanchisquare

rank_diff_list = [-3,-7,1,-2,-7,-1,-2,9,-5,-6,3,-2,-2,-3,-12,-3,-8,-15,-4,-5,-7,-12,
                  -14,-5,-5,-2,-10,-17,4,-1,-2]
ratio_csv = pd.read_csv('/Users/apple/Desktop/projects/Fantasy/Real v Sim Analysis /One vs Random Analysis/Valid.csv')

rank_diff_list_abs = [abs(x) for x in rank_diff_list]
xpoints = np.array(rank_diff_list_abs)
ypoints = np.array(ratio_csv['Real Win/Sim Win'].tolist())


plt.plot(xpoints, ypoints, 'o')
plt.show()

rankdiffmed = statistics.median(rank_diff_list_abs)
ratio_csv['Rank Diff'] = rank_diff_list_abs

rank_diff_more=[]
rank_diff_less=[]
for index, row in ratio_csv.iterrows():
    if(row.iat[5]>=rankdiffmed):
        rank_diff_more.append(row.iat[2])
    else:
        rank_diff_less.append(row.iat[2])

# Mann-Whitney U Test
stat, p = mannwhitneyu(rank_diff_less, rank_diff_more)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')
    

# # Wilcoxon Signed-Rank Test
# stat, p = wilcoxon(rank_diff_less, rank_diff_more)
# print('Statistics=%.3f, p=%.3f' % (stat, p))
# # interpret
# alpha = 0.05
# if p > alpha:
# 	print('Same distribution (fail to reject H0)')
# else:
# 	print('Different distribution (reject H0)')

# Kruskal-Wallis H Test
stat, p = kruskal(rank_diff_less, rank_diff_more)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')

ratio_csv.to_csv('/Users/apple/Desktop/projects/Fantasy/rank_diff.csv')
# # Friedman Test
# stat, p = friedmanchisquare(rank_diff_less, rank_diff_more)
# print('Statistics=%.3f, p=%.3f' % (stat, p))
# # interpret
# alpha = 0.05
# if p > alpha:
# 	print('Same distributions (fail to reject H0)')
# else:
# 	print('Different distributions (reject H0)')

