# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/release20000101_20141231/20000101_20141231.txt", "r")
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
        top = soup.select('.maindetails_center')[0]
        itemprop = top.select('.itemprop')[0].text.encode('utf-8')
        title = " ".join(itemprop.split())
        title = title.decode('utf-8')
        #print title

        request_get = requests.get(link + "business?ref_=tt_dt_bus") 
        response = request_get.text.encode('utf8') 
        box_soup = BeautifulSoup(response)
        #print soup
        table = box_soup.select("#tn15content")[0]
        #print table
        
        #print repr("".join(table.text).split("\n\n")[0].split("\n")[1])
        ele = "".join(table.text).split("\n\n")[0].split("\n")[1]
        if ele == "Budget":
            #print "".join(table.text).split("\n\n")[0].split("\n")[2]
            bud_temp = "".join(table.text).split("\n\n")[0].split("\n")[2]
            m = re.match(r"([^0-9]+)([0-9,]+)(.*)",bud_temp)
            ##print m.groups(), m.groups()[0], m.groups()[1]
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

            params = (pkno, title, currency4b, budget)
            cursor.execute("insert into budget values (?, ?, ?, ?)", params)
            cnxn.commit()
            print params
    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/release20000101_20141231/budget_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/release20000101_20141231/budget_error.txt", 'a')
        error_detail.write(line+'\n')
        error_detail.write(str(e)+'\n')
        error.write(line+'\n')
        error_detail.close()
        error.close()   
f.close()            
cnxn.close()