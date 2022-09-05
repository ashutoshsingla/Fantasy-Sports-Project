#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:16:45 2022

@author: apple
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
import matplotlib.pyplot as plt
import numpy as np

dir_real = "/Users/apple/Desktop/projects/Fantasy/Total Match Stats/"
dir_sim = "/Users/apple/Desktop/projects/Fantasy/sim_perf/"

dir_dest = "/Users/apple/Desktop/projects/Fantasy/chosen/"
dir_fig = "/Users/apple/Desktop/projects/Fantasy/fig/"

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()

for kk in range(8,9):
    name = lsst[kk]
    df = pd.read_csv(dir_real+name+".csv")
    newdf = pd.DataFrame()
    newdf['Name'] = df['CORRECT NAME']
    newdf['ALL_Chosen %'] = (df['All_Chosen']*100.0)/df['All_Total_Teams']
    newdf['ALL_Captain %'] = (df['All_Captain']*100.0)/df['All_Total_Teams']
    newdf['ALL_Vice Captain %'] = (df['All_Vice_Captain']*100.0)/df['All_Total_Teams']
    
    newdf['Chosen %'] = (df['Chosen']*100.0)/df['Total Teams']
    newdf['Captain %'] = (df['Captain']*100.0)/df['Total Teams']
    newdf['Vice Captain %'] = (df['Vice Captain']*100.0)/df['Total Teams']
    
    df_sim = pd.read_csv(dir_sim+name+'.csv')
    dict_chosen = dict(zip(df_sim['CORRECT NAME'], (df_sim['Chosen']*100.0)/(df_sim['Total Teams']*110)))
    dict_c = dict(zip(df_sim['CORRECT NAME'], (df_sim['Captain']*10*100.0)/(df_sim['Total Teams']*110)))
    dict_vc = dict(zip(df_sim['CORRECT NAME'], (df_sim['Vice Captain']*10*100.0)/(df_sim['Total Teams']*110)))
    newdf['Sim_Chosen %'] = newdf['Name'].map(dict_chosen)
    newdf['Sim_Captain %'] = newdf['Name'].map(dict_c)
    newdf['Sim_Vice Captain %'] = newdf['Name'].map(dict_vc)
    newdf.to_csv(dir_dest+name+'.csv')

for kk in range(8,9):
    name = lsst[kk]
    newdf = pd.read_csv(dir_dest+name+'.csv')
    
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
 
    # set height of bar
    chosen = newdf['Chosen %']
    chosen_sim = newdf['Sim_Chosen %']
    
    # Set position of bar on X axis
    br1 = np.arange(len(chosen))
    br2 = [x + barWidth for x in br1]
     
    # Make the plot
    plt.bar(br1, chosen, color ='r', width = barWidth,
            edgecolor ='grey', label ='Real')
    plt.bar(br2, chosen_sim, color ='g', width = barWidth,
            edgecolor ='grey', label ='Sim')
    
    # Adding Xticks
    plt.xlabel('Player', fontweight ='bold', fontsize = 15)
    plt.ylabel('Chosen %', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(chosen))],
            newdf['Name'])
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'valid/chosen/'+name+'.png')
    plt.show()
    
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
    
    capt = newdf['Captain %']
    capt_sim = newdf['Sim_Captain %']
    # Make the plot
    plt.bar(br1, capt, color ='r', width = barWidth,
            edgecolor ='grey', label ='Real')
    plt.bar(br2, capt_sim, color ='g', width = barWidth,
            edgecolor ='grey', label ='Sim')
    
    # Adding Xticks
    plt.xlabel('Player', fontweight ='bold', fontsize = 15)
    plt.ylabel('Captain %', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(capt))],
            newdf['Name'])
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'valid/capt/'+name+'.png')
    plt.show()
    
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
    
    vcapt = newdf['Vice Captain %']
    vcapt_sim = newdf['Sim_Vice Captain %']
    # Make the plot
    plt.bar(br1, vcapt, color ='r', width = barWidth,
            edgecolor ='grey', label ='Real')
    plt.bar(br2, vcapt_sim, color ='g', width = barWidth,
            edgecolor ='grey', label ='Sim')
    
    # Adding Xticks
    plt.xlabel('Player', fontweight ='bold', fontsize = 15)
    plt.ylabel('Vice Captain %', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(vcapt))],
            newdf['Name'])
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'valid/vc_capt/'+name+'.png')
    plt.show()
    