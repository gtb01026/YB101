# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
f = open("C:/Users/BigData/Dropbox/BoxOffice/castok.txt", "r")
file_dic = {}
#count = 0
for line in f.readlines(): 
    #print line
    link = line.strip()
    #print link
    pkno = link.split('/')[4]
    #print pkno
    file_dic[pkno] = 1
    #if pkno not in cast_dic:
        #print pkno
        #count += 1
#print count
        
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
cursor.execute("SELECT DISTINCT pkno FROM genres")
row = cursor.fetchall()
cast_dic = {}
if row:
    for r in row:
        #print r[0]
        cast_dic[r[0]] = 1
        if r[0] not in file_dic:
            print r[0]

cnxn.close()