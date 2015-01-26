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
# 匯入電影圖片頁面連結文字檔
img_list = open("C:/Users/BigData/Dropbox/BoxOffice/temp.txt",'r')
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

        params = (pkno, link_href)
        # print params
        cursor.execute("insert into movie_image_link values (?, ?)", params)
        cnxn.commit()
    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/MILinkError_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/MILinkError.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        error.write(line)
        error_detail.close()
        error.close()
    try:
        jpg = src_link.split('/')[-1]
        # print jpg
        rs = requests.get(link_href,stream=True)
        with open('C:/Users/BigData/Dropbox/BoxOffice/4994movie_image/%s.jpg'%(pkno),'wb')as out_file: #檔名一定要用這樣的格式替換
            shutil.copyfileobj(rs.raw,out_file)
            del rs

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/MIError_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/MIError.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        error.write(line)
        error_detail.close()
        error.close()


img_list.close()
cnxn.close()
