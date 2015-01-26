# -*- coding: utf-8 -*-
"""
Created on Thu Jan 15 09:50:40 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil

img_list = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/temp2.txt",'r')
for line in img_list.readlines():
    cano = line.split('/')[-1].split('?')[0]
    # print cano
    try:
        rs = requests.get(line)
        response = rs.text.encode('utf-8')
        soup = BeautifulSoup(response)
        table = soup.select('.photo')[0]
        src_link = [tag['src'] for tag in table.select('img')][0]
        link_href = urlparse.urljoin("http://www.imdb.com/", src_link)
        
        rs = requests.get(link_href,stream=True)
        with open('E:/cnc_image/%s.jpg'%(cano),'wb')as out_file: #檔名一定要用這樣的格式替換
            shutil.copyfileobj(rs.raw,out_file)
            del rs
        link_herf = ""

    except IndexError, e:
        print line, e
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/CNCIIndex_error.txt", 'a')
        error.write(line + "\n")
        error.close() 
    
    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/CNCI_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/CNCI_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e) + "\n")
        error.write(line + "\n")
        error_detail.close()
        error.close()


img_list.close()
