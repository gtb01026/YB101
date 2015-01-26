# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 22:08:00 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil


cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
# 匯入電影圖片頁面連結文字檔
img_list = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_link.txt",'r')
for line in img_list.readlines():
    pkno = line.split('/')[-1].split('?')[0]
    # print pkno
    try:
        rs = requests.get(line)
        response = rs.text.encode('utf-8')
        soup = BeautifulSoup(response)
        table = soup.select('.photo')[0]
        src_link = [tag['src'] for tag in table.select('img')][0]
        link_href = urlparse.urljoin("http://www.imdb.com/", src_link)
        # print link_href

        params = (link_href, pkno)
        # print params
        cursor.execute("update movie_list \
                        set image_link4movie = ? \
                        where pkno = ?", params)
        cnxn.commit()
    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_list_img_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_list_img_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e)+'\n')
        error.write(line)
        error_detail.close()
        error.close()
    try:
        jpg = src_link.split('/')[-1]
        # print jpg
        rs = requests.get(link_href,stream=True)
        with open('C:/Users/BigData/Desktop/movie_image_1970_2010/%s.jpg'%(pkno),'wb')as out_file: #檔名一定要用這樣的格式替換
            shutil.copyfileobj(rs.raw,out_file)
            del rs

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_error.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e)+'\n')
        error.write(line)
        error_detail.close()
        error.close()


img_list.close()
cnxn.close()

