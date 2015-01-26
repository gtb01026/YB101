# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
request_get = requests.get("http://www.imdb.com/name/nm0163988")
# print request_get
response = request_get.text.encode('utf8')
soup = BeautifulSoup(response)
div = soup.select('.image')[0]
cast_link = [tag['href'] for tag in div.select('a')][0]
link_href = urlparse.urljoin("http://www.imdb.com/", cast_link)
print link_href