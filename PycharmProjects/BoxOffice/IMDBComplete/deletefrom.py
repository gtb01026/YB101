# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 15:37:54 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/temp.txt", "r")
for line in f.readlines():
        link = line.strip()
#        pkno = link.split('/')[-1].split('?')[0]
#        cursor.execute("update movie_list set image_link4movie = NULL where pkno = ?", pkno)
        pkno = link.split('/')[4]
        cursor.execute("delete from locations where pkno = ?", pkno)
        cnxn.commit()
f.close()
cnxn.close()


