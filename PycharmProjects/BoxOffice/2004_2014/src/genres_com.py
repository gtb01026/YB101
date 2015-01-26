# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
#cursor = cnxn.cursor()
path = "C:/Users/BigData/Dropbox/BoxOffice/bid_list/"
filenames = os.listdir(path)
for filename in filenames:
    f = open(path + filename, "r")
    for line in f.readlines():
        #try:
            link = line.strip()
            pkno = link.split('/')[4]
            #print pkno

            rs = requests.session()
            request_get = requests.get(link)
            response = request_get.text.encode('utf8')
            soup = BeautifulSoup(response)
            maindetails = soup.select('.maindetails_center')[0]
            itemprop = maindetails.select('.itemprop')[0].text.encode('utf-8')
            title = " ".join(itemprop.split())
            #title_code = str([title])[2:-2]
            title_code = title.decode('utf-8')

            #print title_code

            StoryLine = soup.select('#titleStoryLine')[0]
            div_coll = StoryLine.select('div')
            for div in div_coll:
                h4_coll = div.select('h4')
                for h4 in h4_coll:
                    if h4.text == 'Genres:':
                        a_coll = div.select('a')
                        priority4g = 1
                        for a in a_coll:
                            genre = a.text.strip()
                            params = (pkno, title_code, priority4g, genre)
                            #cursor.execute("insert into genres values (?, ?, ?, ?)", params)
                            #cnxn.commit()
                            print params
                            priority4g += 1


        #except BaseException, e:
            #print line, e
            #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/genresCom_error_detail.txt", 'a')
            #error = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/genresCom_error.txt", 'a')
            #error_detail.write(line)
            #error_detail.write(str(e))
            #error.write(line)
            #error_detail.close()
            #error.close()

    f.close()
#cnxn.close()

