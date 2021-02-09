# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 20:27:15 2020

@author: 64584
"""

import os 
import pandas as pd
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

def data(file):
    title = file.iloc[:,0].dropna().tolist()
    comment = file.iloc[:,0].dropna().tolist()
    
    
    data = [title,comment]
    pos = []
    sub = []
    
    for item in data :
        for phrase in item :
            blob = TextBlob(phrase, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
            sen = blob.sentiment
            pos.append(sen[0])
            sub.append(sen[1])
            print(phrase)
            print(sen)

path = "C:/Users/64584/Desktop/ADH/BORDEAUX"
files = os.listdir(path)

for f in files :
    f_in = pd.read_excel(path+"/"+f)
    data(f_in)
    