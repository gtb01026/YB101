# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 20:32:37 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time

def get_title(link):
    request_get = requests.get(link)
    response = request_get.text.encode('utf8')
    soup = BeautifulSoup(response)
    top = soup.select('.maindetails_center')[0]
    itemprop = top.select('.itemprop')[0].text.encode('utf-8')
    title_unde = " ".join(itemprop.split())
    title = title_unde.decode('utf-8')
    return title


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/temp.txt", "r")
for line in f.readlines():
    try:
        link = line.strip()
        pkno = link.split('/')[4]
        rs = requests.session()
        title = get_title(link)
        params = (pkno, title)
        cursor.execute("insert into movie_list values (?, ?, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)", params)
        cnxn.commit()
        print params

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/pkno_title_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/pkno_title_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e)+'\n')
        error.write(line)
        error_detail.close()
        error.close()

f.close()
cnxn.close()


