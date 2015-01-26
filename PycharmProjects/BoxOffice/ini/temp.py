# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
#f = open("C:/Users/BigData/Dropbox/BoxOffice/4994.txt", "r")
f = open("C:/Users/BigData/Dropbox/BoxOffice/castcanoerror.txt", "r")
for line in f.readlines():
    try:
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
        title_unde = " ".join(itemprop.split())
        title = title_unde.decode('utf-8')
        #print type(title)

        request_get = requests.get(link + "fullcredits?ref_=tt_ov_wr#writers")
        response = request_get.text.encode('utf8')
        box_soup = BeautifulSoup(response)
        #print soup
        fullcredits = box_soup.select("#fullcredits_content")[0]
        cast_list = fullcredits.select(".cast_list")[0]
        tr_coll = cast_list.select("tr")[1:]
        priority4cast = 1
        for tr in tr_coll:
            td_coll = tr.select('td')
            if td_coll[0].text == "Rest of cast listed alphabetically:":
                break
            else:
                cast = td_coll[1].text.strip()
                #print type(cast)
                #cast = str(cast_unde).decode('utf-8')
                cast_link = [tag['href'] for tag in td_coll[1].select('a')][0]
                cano = cast_link.split('/')[2]
                params = (pkno, title, priority4cast, cano, cast)
                cursor.execute("insert into cast values (?, ?, ?, ?, ?)", params)
                cnxn.commit()
                print params
                priority4cast += 1

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/casterror_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/castcanoerror.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        error.write(line)
        error_detail.close()
        error.close()

f.close()
cnxn.close()