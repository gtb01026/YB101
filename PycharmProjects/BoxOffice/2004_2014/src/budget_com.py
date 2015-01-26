# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

#cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
#cursor = cnxn.cursor()

path = "C:/Users/BigData/Dropbox/BoxOffice/bid_list/"
filenames = os.listdir(path)
for filename in filenames:
    yearinimdb = filename.split('.')[0]
    f = open(path + filename, "r")
    #f = open("C:/Users/BigData/Dropbox/BoxOffice/a.txt", "r")
    for line in f.readlines():
        #try:
            link = line.strip()
            pkno = link.split('/')[4]
            #print pkno

            rs = requests.session()
            request_get = requests.get(link)
            response = request_get.text.encode('utf8')
            soup = BeautifulSoup(response)
            top = soup.select('.maindetails_center')[0]
            itemprop = top.select('.itemprop')[0].text.encode('utf-8')
            title = " ".join(itemprop.split())
            #title_code = str([title])[2:-2]
            title_code = title.decode('utf-8')
            #print title_code

            request_get = requests.get(link + "business?ref_=tt_dt_bus")
            response = request_get.text.encode('utf8')
            box_soup = BeautifulSoup(response)
            table = box_soup.select("#tn15content")[0]
            ele = "".join(table.text).split("\n\n")[0].split("\n")[1]
            if ele == "Budget":
                bud_temp = "".join(table.text).split("\n\n")[0].split("\n")[2]
                m = re.match(r"([^0-9]+)([0-9,]+)(.*)",bud_temp)
                currency4b = m.groups()[0].strip()
                budget = m.groups()[1].strip().replace(",", "")
                #print currency4b
                #print budget
                if currency4b == "$":
                    currency4b = "USD"
                elif currency4b == "$CAD":
                    currency4b = "CAD"
                elif str([currency4b])[4:-2] == "xa3":
                    currency4b = "GBP"
                elif str([currency4b])[4:-2] == "u20ac":
                    currency4b = "EUR"
                elif str([currency4b])[4:-2] == "xa5":
                    currency4b = "JPY"

                params = (pkno, title_code, currency4b, budget, yearinimdb)
                #cursor.execute("insert into budget values (?, ?, ?, ?, ?)", params)
                #cnxn.commit()
                print params

        #except BaseException, e:
            #print line, e
            #error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/budgetCom_error_detail.txt", 'a')
            #error = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/budgetCom_error.txt", 'a')
            #error_detail.write(line)
            #error_detail.write(str(e))
            #error.write(line)
            #error_detail.close()
            #error.close()
    f.close()
#cnxn.close()