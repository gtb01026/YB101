# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 20:43:44 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_link.txt", 'a')
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/temp.txt", "r")
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

        maindetails = soup.select('.maindetails_center')[0]
        itemprop = maindetails.select('.itemprop')[0].text.encode('utf-8')
        title = " ".join(itemprop.split())
        #print title

        div = soup.select('.image')[0]
        cast_link = [tag['href'] for tag in div.select('a')][0]
        link_href = urlparse.urljoin("http://www.imdb.com/", cast_link)
#        if link_href == "http://www.imdb.com/awards-central/video/?ref_=tt_tt_edw_FreshTakes_i_1":
#            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_link_error_detail02.txt", 'a')
#            error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_link_error02.txt", 'a')
#            error_detail.write(line)
#            error_detail.write(link_href+'\n')
#            error.write(line)
#            error_detail.close()
#            error.close()
#        else:
        print link_href
        bid_file.write(link_href+'\n')
        

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_link_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_link_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e)+'\n')
        error.write(line)
        error_detail.close()
        error.close()

f.close()
bid_file.close()



