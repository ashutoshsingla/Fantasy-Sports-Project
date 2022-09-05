#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 19:25:48 2022

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

dir1 = "/Users/apple/Desktop/projects/Fantasy/chosen/"
dir2 = "/Users/apple/Desktop/projects/Fantasy/Count/"
dir_fig = "/Users/apple/Desktop/projects/Fantasy/FigFolder/"

matchdf = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/match_names.csv")    
lsst = matchdf["Match"].tolist()
tot_team_count = []
for name in lsst:
    df = pd.read_csv("/Users/apple/Desktop/projects/Fantasy/Total Match Stats/"+name+".csv")
    tot_team_count.append(df.iloc[1,-1])

for kk in range(1,31):
    name = lsst[kk]
    newdf = pd.read_csv(dir1+name+'.csv')
    newdf2 = pd.read_csv(dir2+name+'.csv')
    newdf.drop(df.columns[0], axis = 1, inplace = True)
    newdf2.drop(df.columns[0], axis = 1, inplace = True)
    list_name = newdf['Name'].tolist()
    sim_p = newdf['Sim_Chosen %'].tolist()
    sim_c = newdf['Sim_Captain %'].tolist()
    sim_vc = newdf['Sim_Vice Captain %'].tolist()
    
    real_p = []
    real_c = []
    real_vc = []
    
    name_dict = {}
    for nm in list_name:
        name_dict[nm]=0
    real_dict = {}
    for i in range(0,len(newdf2)):
        real_dict[newdf2.iloc[i,0]]=i
    for nam in list_name:
        real_p.append(newdf2.iloc[real_dict[nam],1]*100/tot_team_count[kk])
        real_c.append(newdf2.iloc[real_dict[nam],2]*100/tot_team_count[kk])
        real_vc.append(newdf2.iloc[real_dict[nam],3]*100/tot_team_count[kk])
    for i in range(0,len(newdf2)):
        if not newdf2.iloc[i,0] in name_dict:
            sim_p.append(0)
            sim_c.append(0)
            sim_vc.append(0)
            real_p.append(newdf2.iloc[i,1]*100/tot_team_count[kk])
            real_c.append(newdf2.iloc[i,2]*100/tot_team_count[kk])
            real_vc.append(newdf2.iloc[i,3]*100/tot_team_count[kk])
            name_dict[newdf2.iloc[i,0]]=0
    name_list = name_dict.keys()
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
 
    # set height of bar
    chosen = real_p
    chosen_sim = sim_p
    
    # Set position of bar on X axis
    br1 = np.arange(len(real_p))
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
            name_list)
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'chosen/'+name+'.png')
    plt.show()
    
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
    
    capt = real_c
    capt_sim = sim_c
    # Make the plot
    plt.bar(br1, capt, color ='r', width = barWidth,
            edgecolor ='grey', label ='Real')
    plt.bar(br2, capt_sim, color ='g', width = barWidth,
            edgecolor ='grey', label ='Sim')
    
    # Adding Xticks
    plt.xlabel('Player', fontweight ='bold', fontsize = 15)
    plt.ylabel('Captain %', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(capt))],
            name_list)
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'capt/'+name+'.png')
    plt.show()
    
    # set width of bar
    barWidth = 0.25
    fig = plt.subplots(figsize =(24, 16))
    
    vcapt = real_vc
    vcapt_sim = sim_vc
    # Make the plot
    plt.bar(br1, vcapt, color ='r', width = barWidth,
            edgecolor ='grey', label ='Real')
    plt.bar(br2, vcapt_sim, color ='g', width = barWidth,
            edgecolor ='grey', label ='Sim')
    
    # Adding Xticks
    plt.xlabel('Player', fontweight ='bold', fontsize = 15)
    plt.ylabel('Vice Captain %', fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(vcapt))],
            name_list)
    plt.xticks(rotation=90)
    plt.title(name)
    plt.legend()
    plt.savefig(dir_fig+'vc_capt/'+name+'.png')
    plt.show()
    thisdf = pd.DataFrame()
    thisdf['Name']=name_list
    thisdf['realChosen%']=real_p
    thisdf['realCaptain%']=real_c
    thisdf['ealViceCaptain']=real_vc
    thisdf['simChosen%']=sim_p
    thisdf['simCaptain%']=sim_c
    thisdf['simViceCaptain%']=sim_vc
    #thisdf.to_csv('/Users/apple/Desktop/projects/Fantasy/demo.csv')
