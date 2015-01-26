# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

f = open("C:/Users/BigData/Dropbox/BoxOffice/a2.txt", "r")
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
        print link_href
        bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/4994movie_img_link.txt", 'a')
        bid_file.write(link_href + "\n")
        bid_file.close()

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/MILinkError_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/MILinkError.txt", 'a')
        error_detail.write(line+'\n')
        error_detail.write(str(e)+'\n')
        error.write(line+'\n')
        error_detail.close()
        error.close()

f.close()
#cnxn.close()


