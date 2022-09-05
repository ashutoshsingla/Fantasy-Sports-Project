#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 17:43:18 2022

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

df = pd.read_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/one_on_one_valid_match.csv") 

df['Real/Sim Ratio'] = df['Real Win Prob'] / ( 1 - df['Real Win Prob'])

df.to_csv("/Users/ashutoshsingla/Desktop/Fantasy_Project/one_on_one_valid_match.csv")
