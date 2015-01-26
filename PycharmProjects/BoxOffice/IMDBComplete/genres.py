# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 16:00:59 2015

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
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/temp.txt", "r")
for line in f.readlines():
    try:
        link = line.strip()
        pkno = link.split('/')[4]
        # print pkno
        rs = requests.session()
        title = get_title(link)
    #        print type(title)
    
        request_get = requests.get(link)
        response = request_get.text.encode('utf8')
        soup = BeautifulSoup(response)
        StoryLine = soup.select('#titleStoryLine')[0]
        #print top
        div_coll = StoryLine.select('div')
        for div in div_coll:
            h4_coll = div.select('h4')
            for h4 in h4_coll:
                if h4.text == 'Genres:':
                    a_coll = div.select('a')
                    priority4g = 1
                    for a in a_coll:
                        genre = a.text.strip()
                        params = (pkno, title, priority4g, genre)
                        cursor.execute("insert into genres values (?, ?, ?, ?)", params)
                        cnxn.commit()
                        print params
                        priority4g += 1


    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/genres_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/genres_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e)+'\n')
        error.write(line)
        error_detail.close()
        error.close()

f.close()
cnxn.close()


