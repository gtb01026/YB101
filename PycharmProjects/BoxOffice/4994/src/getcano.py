#%%
# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil

list = open("C:/Users/BigData/Dropbox/BoxOffice/CILinkIndexError.txt",'r')
for line in list.readlines():
    cano = line.split('/')[-1].split('?')[0]
    # print cano
    bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/temp.txt", 'a')
    bid_file.write(cano)
    bid_file.close()

list.close()

#%%