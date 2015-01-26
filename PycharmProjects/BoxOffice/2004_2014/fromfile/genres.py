# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
#cursor = cnxn.cursor()
path = "C:/Users/BigData/Dropbox/BoxOffice/4994movie_detail/"
filenames = os.listdir( path )
#setup_table(cur)
count = 1
for filename in filenames:
    #print filename
    f = open(path + filename, 'r')
    response_text = f.read()
    f.close()
    soup = BeautifulSoup(response_text)
    #print soup
    pkno = filename.split(".txt")[0]
    print pkno
    maindetails = soup.select('.maindetails_center')[0]
    itemprop = maindetails.select('.itemprop')[0].text.encode('utf-8')
    title = " ".join(itemprop.split())
    #print title

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
                    #cursor.execute("insert into genres values (?, ?, ?, ?)", params)
                    #cnxn.commit()
                    print params
                    priority4g += 1


    #except BaseException, e:
        #print line, e
        #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/genreserror_detail.txt", 'a')
        #error = open("C:/Users/BigData/Dropbox/BoxOffice/temp.txt", 'a')
        #error_detail.write(line)
        #error_detail.write(str(e))
        #error.write(line)
        #error_detail.close()
        #error.close()

#cnxn.close()

