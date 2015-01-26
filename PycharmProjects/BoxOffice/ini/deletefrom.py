# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
        
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.120.28.11;DATABASE=IMDB')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/locationserror.txt", "r")
for line in f.readlines():
    try:
        #print line
        link = line.strip()
        #print link
        pkno = link.split('/')[4]
        #print pkno

        cursor.execute("delete from locations where pkno = ?", pkno)
        cnxn.commit()

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/temp2.txt", 'a')
        #error = open("C:/Users/BigData/Dropbox/BoxOffice/locationserror.txt", 'a')
        error_detail.write(line)
        error_detail.write(str(e))
        #error.write(line)
        error_detail.close()
        #error.close()
        
f.close()
cnxn.close()