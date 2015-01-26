# -*- coding: utf-8 -*-
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


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/4994link.txt", "r")
for line in f.readlines():
    try:
        link = line.strip()
        pkno = link.split('/')[4]
        # print pkno
        rs = requests.session()
        title = get_title(link)
        # print title
        params = (pkno, title)
        cursor.execute("insert into title_decode values (?, ?)", params)
        cnxn.commit()
        print params

    # except IndexError, e:
    #     print line, e
    except BaseException, e:
        print line, e
        # error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/temp3.txt", 'a')
        # error_detail.write(line)
        # error_detail.write(str(e))
        error.write(line)
        # error_detail.close()
        error.close()

f.close()
cnxn.close()
