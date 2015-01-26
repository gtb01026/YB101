# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 13:15:38 2015

@author: BigData
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 22:08:00 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
# 匯入電影圖片頁面連結文字檔
f = open("C:/Users/BigData/Desktop/HistoricalRate.csv",'r')
#country = f.readlines()[0].split(',')
#print country
for line in f.readlines()[1:-8]:
    params = line.split(',')
    params[0] = params[0].replace('/', '-')
    params[-1] = params[-1].split('\n')[0]
    print params
    cursor.execute("insert into historical_rate values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
    cnxn.commit()
#    except BaseException, e:
#        print line, e
#        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_error_detail.txt", 'a')
#        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_error.txt", 'a')
#        error_detail.write(line)
#        error_detail.write(str(e)+'\n')
#        error.write(line)
#        error_detail.close()
#        error.close()


f.close()
cnxn.close()


