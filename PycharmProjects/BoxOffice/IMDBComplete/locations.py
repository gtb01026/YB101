# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 21:19:09 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
        
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.120.28.11;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/temp.txt", "r")
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
        title_code = " ".join(itemprop.split())
        title = title_code.decode('utf-8')
        #print type(title)

        request_get = requests.get(link + "locations?ref_=tt_dt_dt")
        response = request_get.text.encode('utf8') 
        box_soup = BeautifulSoup(response)
        #print soup
        fullcredits = box_soup.select("#filming_locations_content")[0]
        #print fullcredits
        div_coll = fullcredits.select("div")[3:]
        i = 0
        for div in div_coll:
            # print div
            a_coll =  div.select('a')
            if i%2 == 0:
                locations = a_coll[0].text.split('\n')[0].strip()
                #print type(locations)
                geo = locations.split(', ')
                country = geo[-1]
                try:
                    state = geo[-2]
                except:
                    state = '99999'
                try:
                    city = geo[-3]
                except:
                    city = '99999'
                # print country
                # print state
                # print city
                interest = a_coll[1].text.strip()
                #print interest
                if interest != 'Is this interesting?':
                    m = re.match(r'([0-9]*) of ([0-9]*)[a-z ]', interest)
                    #print m.groups(), m.group(1), m.group(2)
                    numerator = m.group(1)
                    denominator = m.group(2)
                    fraction = float(m.group(1).decode('utf-8'))/float(m.group(2).decode('utf-8'))
                    #print fraction

                    params = (pkno, title, country, state, city, locations, numerator, denominator, fraction)
                    # print params
                    cursor.execute("insert into locations values (?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
                    cnxn.commit()

            i += 1

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/locations_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/locations_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        error.write(line)
        error_detail.close()
        error.close()
        
f.close()
cnxn.close()
