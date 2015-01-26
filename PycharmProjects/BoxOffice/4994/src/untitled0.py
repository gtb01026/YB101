# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 14:11:33 2015

@author: BigData
"""
#%%
# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
# 匯入演員圖片頁面連結文字檔
img_list = open("C:/Users/BigData/Dropbox/BoxOffice/4994director_img_page_link.txt",'r')
for line in img_list.readlines():
    cano = line.split('/')[-1].split('?')[0]
    # print cano.
    
    rs = requests.get(line)
    response = rs.text.encode('utf-8')
    soup = BeautifulSoup(response)
    table = soup.select('.photo')[0]
    src_link = [tag['src'] for tag in table.select('img')][0]
    link_href = urlparse.urljoin("http://www.imdb.com/", src_link)
    # print link_href

#    jpg = src_link.split('/')[-1]
    # print jpg
    rs = requests.get(link_href,stream=True)
    with open('C:/Users/BigData/Desktop/%s.jpg'%(cano),'wb')as out_file: #檔名一定要用這樣的格式替換
        shutil.copyfileobj(rs.raw,out_file)
        del rs
#    jpg = 0

img_list.close()
cnxn.close()
#%%
