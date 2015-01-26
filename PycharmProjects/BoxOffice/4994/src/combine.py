# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

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
# 匯入4994筆電影主頁連結文字檔
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/1970_2010_01.txt", "r")
for line in f.readlines():
    try:
        link = line.strip()
        pkno = link.split('/')[4]
        # print pkno
        rs = requests.session()
        title = get_title(link)
        # print title
        request_get = requests.get(link + "fullcredits?ref_=tt_ov_wr#writers")
        response = request_get.text.encode('utf8') 
        box_soup = BeautifulSoup(response)
        #print soup
        fullcredits = box_soup.select("#fullcredits_content")[0]
        h4_coll = fullcredits.select("h4")
        table_coll = fullcredits.select("table")
        for i in range(3):
            #print repr(h4_coll[i].text.strip())
            a = re.match(r'([a-z|A-Z]+)' '?.*', h4_coll[i].text.strip())
            #print a.groups(1)
            #print repr(h4_coll[i].text.split('\n')[0])
            priority4w = 1
            if a.groups(1)[0] == 'Directed' or a.groups(1)[0] == 'Writing' or a.groups(1)[0] == 'Produced':
                #print "\n~~~~~~~~~\n"
                #print a.groups(1)[0]
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
                        cast_link = [tag['href'] for tag in td[0].select('a')][0]
                        cano = cast_link.split('/')[2]
                        print type(temp)
                        params = (pkno, title, type4t, priority4w, cano, temp)
                        print params
                        cursor.execute("insert into combine values (?, ?, ?, ?, ?, ?)", params)
                        cnxn.commit()
                        priority4w += 1

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/combine_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/combine_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        error.write(line)
        error_detail.close()
        error.close()
        
f.close()
cnxn.close()