# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time
        
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
            top = soup.select('.maindetails_center')[0]
            itemprop = top.select('.itemprop')[0].text.encode('utf-8')
            title = " ".join(itemprop.split())
            #title_code = str([title])[2:-2]
            title_code = title.decode('utf-8')
            #print title_code

            request_get = requests.get(link + "fullcredits?ref_=tt_ov_wr#writers")
            response = request_get.text.encode('utf8')
            box_soup = BeautifulSoup(response)
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
                    cast_code = str([cast])[3:-2]
                    #print cast_code
                    params = (pkno, title_code, priority4cast, cast_code, "99999")
                    #cursor.execute("insert into cast values (?, ?, ?, ?, ?)", params)
                    #cnxn.commit()
                    print params
                    priority4cast += 1

        #except BaseException, e:
            #print line, e
            #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/castCom_error_detail.txt", 'a')
            #error = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/castCom_error.txt", 'a')
            #error_detail.write(line)
            #error_detail.write(str(e))
            #error.write(line)
            #error_detail.close()
            #error.close()

    f.close()
#cnxn.close()
            