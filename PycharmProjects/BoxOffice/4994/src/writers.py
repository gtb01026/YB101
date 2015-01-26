# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
        
#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
#cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/writerserror.txt", "r")
for line in f.readlines():
    #try:
        #print line
        link = line.strip()
        #print link
        pkno = link.split('/')[4]
        #print pkno

        rs = requests.session()
        request_get = requests.get(link)
        #print request_get
        response = request_get.text.encode('utf8') 
        soup = BeautifulSoup(response)
        top = soup.select('.maindetails_center')[0]
        itemprop = top.select('.itemprop')[0].text.encode('utf-8')
        title = " ".join(itemprop.split())
        #print title

        request_get = requests.get(link + "fullcredits?ref_=tt_ov_wr#writers") 
        response = request_get.text.encode('utf8') 
        box_soup = BeautifulSoup(response)
        #print soup
        fullcredits = box_soup.select("#fullcredits_content")[0]
        table_coll = fullcredits.select("table")[1:2]
        priority4w = 1
        for eachtable in table_coll:
            tr_coll = eachtable.select("tr")
            for eachtr in tr_coll:
                td = eachtr.select("td")
                writer = td[0].text.strip()
                if writer != "":
                    params = (pkno, title, priority4w, writer)
                    print params
                    #cursor.execute("insert into writers values (?, ?, ?, ?)", params)
                    #cnxn.commit()
                    priority4w += 1

    #except BaseException, e:
        #print line, e
        #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/temp.txt", 'a') 
        #error = open("C:/Users/BigData/Dropbox/BoxOffice/writerserror.txt", 'a') 
        #error_detail.write(line)
        #error_detail.write(str(e))
        #error.write(line)
        #error_detail.close()
        #error.close()
        
#f.close()            
#cnxn.close()