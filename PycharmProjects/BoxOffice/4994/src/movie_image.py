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

path = "C:/Users/BigData/Dropbox/BoxOffice/4994movie_image/"
filenames = os.listdir(path)
for filename in filenames:
    print path + filename
    f = open(path + filename, "rb")
    ablob = pyodbc.Binary(f.read().encode('hex'))
    pkno = filename.split('.')[0]
    print pkno
    params = ( "123" + pkno, ablob)
    print params
    # cursor.execute("insert into movie_image values (?, ?)", params)
    # cnxn.commit()


    # except BaseException, e:
    #     print line, e
    #     error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/combineerror_detail.txt", 'a')
    #     error = open("C:/Users/BigData/Dropbox/BoxOffice/combineerror.txt", 'a')
    #     error_detail.write(line)
    #     error_detail.write(str(e))
    #     error.write(line)
    #     error_detail.close()
    #     error.close()

cnxn.close()