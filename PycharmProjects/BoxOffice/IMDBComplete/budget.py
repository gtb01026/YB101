# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 16:59:41 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc

def get_month(v):
    month = 0
    if v == 'January':
        month = 1
    elif v == 'February':
        month = 2
    elif v == 'March':
        month = 3
    elif v == 'April':
        month = 4
    elif v == 'May':
        month = 5
    elif v == 'June':
        month = 6
    elif v == 'July':
        month = 7
    elif v == 'August':
        month = 8
    elif v == 'September':
        month = 9
    elif v == 'October':
        month = 10
    elif v == 'November':
        month = 11
    elif v == 'December':
        month = 12
    return month

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_02.txt", "r")
for line in f.readlines(): 
#    try:
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

        rs = requests.session()        
        request_get = requests.get(link + "business?ref_=tt_dt_bus") 
        response = request_get.text.encode('utf8') 
        box_soup = BeautifulSoup(response)
#        print soup
        table = box_soup.select("#tn15content")[0]
        #print table
        
        ele02_coll = "".join(table.text).split("\n\n")
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
            cursor.execute("insert into budget02 values (?, ?, ?, ?)", params)
            cnxn.commit()
            print params            
                        
#            for ele02 in ele02_coll:
#                if ele02.split("\n")[0] == "Filming Dates":
##                    print repr(ele02.split("\n")[1].encode('utf-8'))
#                    try:
#                        date_coll = ele02.split("\n")[1].encode('utf-8').split("\xc2\xa0-\xc2\xa0")
#    #                    if date_coll = ele02.split("\n")[1].encode('utf-8').split("\xc2\xa0-\xc2\xa0") is not None:
#    #                    print date_coll
#                        filming_date_from_day = date_coll[0].split(" ")[0]
#                        v = date_coll[0].split(" ")[1]
#                        filming_date_from_month = get_month(v)
#                        filming_date_from_year = date_coll[0].split(" ")[2]
#                        filming_date_to_day = date_coll[1].split(" ")[0]
#                        w = date_coll[1].split(" ")[1]
#                        filming_date_to_month = get_month(w)
#                        filming_date_to_year = date_coll[1].split(" ")[2]
#                        
#                        filming_date_from = filming_date_from_year + "-" + str(filming_date_from_month) + "-" + filming_date_from_day
#                        filming_date_to = filming_date_to_year + "-" + str(filming_date_to_month) + "-" + filming_date_to_day
#    #                    print filming_date_from
#    #                    print filming_date_to
#                        
#                        params = (filming_date_from, filming_date_to, pkno)
#                        cursor.execute("update budget02 set filming_date_from = ?, filming_date_to = ? where pkno = ?", params)
#                        cnxn.commit()
#                        print params
#                        break
#                        
#                    except IndexError, e:
#                        date = ele02.split("\n")[1].encode('utf-8').split(" ")
##                        print date
#                        filming_date_to_day = '28'
#                        if date[0] != "":
#                            filming_date_to_day = date[0]
#                        w = date[1]
#                        filming_date_to_month = get_month(w)
#                        filming_date_to_year = date[2]
#                        
#                        filming_date_to = filming_date_to_year + "-" + str(filming_date_to_month) + "-" + filming_date_to_day
#                        
#                        params = (filming_date_to, pkno)
#                        cursor.execute("update budget02 set filming_date_to = ? where pkno = ?", params)
#                        cnxn.commit()
#                        print params
#                        break
            

#    except BaseException, e:
#        print line, e
#        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/budget_error_detail.txt", 'a')
#        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/budget_error.txt", 'a')
#        error_detail.write(line)
#        error_detail.write(str(e)+'\n')
#        error.write(line)
#        error_detail.close()
#        error.close()   
f.close()            
cnxn.close()
