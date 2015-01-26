# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 21:43:15 2015

@author: BigData
"""
#%%
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time
#%%
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
cursor.execute("SELECT cano FROM castncrew_list WHERE cano > 'nm3506834' ORDER BY cano")
cano_coll = cursor.fetchall()
#%%
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/temp.txt", "r")
for cano in f.readlines():
#for cano in cano_coll:
    #print type(cano)
    cano = cano.strip()
    print cano
    try:
        bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/cnc_img_page_link.txt", 'a')
        rs = requests.session()
        request_get = requests.get("http://www.imdb.com/name/"+cano)
        # print request_get
        response = request_get.text.encode('utf8')
        soup = BeautifulSoup(response)
        div = soup.select('.image')[0]
        cast_link = [tag['href'] for tag in div.select('a')][0]
        link_href = urlparse.urljoin("http://www.imdb.com/", cast_link)
        print link_href
        bid_file.write(link_href + "\n")
        bid_file.close()

    except IndexError, e:
        print cano[0], e
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/cnc_img_page_link_indexerror.txt", 'a')
        error.write(cano + "\n")
        error.close()  

    except BaseException, e:
        print cano[0], e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/cnc_img_page_link_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/cnc_img_page_link_error.txt", 'a')
        error_detail.write(cano)
        error_detail.write(str(e) + "\n")
        error.write(cano + "\n")
        error_detail.close()
        error.close()


#f.close()
cnxn.close()

