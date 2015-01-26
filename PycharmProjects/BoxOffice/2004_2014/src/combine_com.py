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
            h4_coll = fullcredits.select("h4")
            table_coll = fullcredits.select("table")
            for i in range(3):
                a = re.match(r'([a-z|A-Z]+)' '?.*', h4_coll[i].text.strip())
                priority4w = 1
                if a.groups(1)[0] == 'Directed' or a.groups(1)[0] == 'Writing' or a.groups(1)[0] == 'Produced':
                    if a.groups(1)[0] == 'Directed':
                        type4t = 'director'
                    if a.groups(1)[0] == 'Writing':
                        type4t = 'writer'
                    if a.groups(1)[0] == 'Produced':
                        type4t = 'producer'
                    tr_coll = table_coll[i].select("tr")
                    for eachtr in tr_coll:
                        td = eachtr.select("td")
                        if td[0].text.strip():
                            temp = td[0].text.strip()
                            temp_code = str([temp])[3:-2]
                            #print temp_code

                            params = (pkno, title_code, type4t, priority4w, temp_code)
                            print params
                            #cursor.execute("insert into combine values (?, ?, ?, ?, ?)", params)
                            #cnxn.commit()
                            priority4w += 1

        #except BaseException, e:
            #print line, e
            #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/combineCom_error_detail.txt", 'a')
            #error = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/combineCom_error.txt", 'a')
            #error_detail.write(line)
            #error_detail.write(str(e))
            #error.write(line)
            #error_detail.close()
            #error.close()

    f.close()
#cnxn.close()