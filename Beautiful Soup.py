#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 09:55:21 2019

@author: princ
"""

from urllib.request import urlopen
html=urlopen("https://database.lichess.org")
import bs4 as BeautifulSoup
soup = BeautifulSoup.BeautifulSoup(html,'html.parser')
ref=soup.findAll("a")
get=[]
for aRef in ref:
    line = str(aRef)
    if "standard" in line :
       get.append(line)
print(len(get))
print(get)