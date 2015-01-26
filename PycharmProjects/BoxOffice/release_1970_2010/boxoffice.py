# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 17:00:53 2015

@author: BigData
"""
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
        #ele = "".join(table.text).split("\n\n")[0].split("\n")[1]
        #if ele == "Budget":
            #print "".join(table.text).split("\n\n")[0].split("\n")[2]
            #bud_temp = "".join(table.text).split("\n\n")[0].split("\n")[2]
            #m = re.match(r"([^0-9]+)([0-9,]+)(.*)",bud_temp)
            ##print m.groups(), m.groups()[0], m.groups()[1]
            #currency4b = m.groups()[0].strip()
            #budget = m.groups()[1].strip()
            #print currency4b
            #print budget
        
        for part in "".join(table.text).split("\n\n"):
            #print repr(part.split("\n")[0])
            ele2 = part.split("\n")[0]
            if ele2 == "Weekend Gross":
                #print repr(part.split("\n")[1].split(" ("))
                aaa = part.split("\n")[1].split(")")
                #print aaa
                i = 0
                aspl_dic = {}
                for a in aaa:
                    #print a
                    #print repr(a.split(" ("))
                    #print a.split(" (")
                    #print len(aaa)
                    aspl_dic[i] = a.split(" (")
                    i += 1

                #print aspl_dic
                #print len(aspl_dic)
                #print aspl_dic[j][1]
                #print aspl_dic[j+2][1]
                wg_dic = {}
                k = 1
                for j in range(len(aspl_dic)-2, -1, -1):
                    if aspl_dic[j][1] == "USA":
                        #print aspl_dic[j][0]
                        #print aspl_dic[j+1][1]
                        #print aspl_dic[j+2][1]
#                        print len(aspl_dic[j+2])
                        if len(aspl_dic[j+2]) == 2:
                            n = re.match(r"([0-9, ]*)([^0-9]+)", aspl_dic[j+2][1])
                            try:    
                                scr = n.groups()[1].strip()
                            except:
                                print("\nexcept!\n")
                            else:
                                if scr  ==  "Screens" or scr  ==  "Screen":
                                    screens = n.groups()[0].strip().replace(",", "")
                                else:
                                    screens = 99999
                        else:
                            screens = 99999
                        #print aspl_dic[j][0]
                        m = re.match(r"([^0-9]+)([0-9,]+)",aspl_dic[j][0])
                        #print m.groups()[0].strip(), m.groups()[1].strip()
                        currency4wg = m.groups()[0].strip()
                        weekendgross = m.groups()[1].strip().replace(",", "")
                        #print aspl_dic[j+1][1].split(" ")[1]
                        day = str(aspl_dic[j+1][1].split(" ")[0])
                        if day == "":
                            day = str(5)
                        year = str(aspl_dic[j+1][1].split(" ")[2])
                        v = aspl_dic[j+1][1].split(" ")[1]
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

                        date = year + "-" + str(month) + "-" + day

                        #print repr(str([currency4wg])[4:-2])
                        #print repr("xa3")
                        if currency4wg == "$":
                            currency4wg = "USD"
                        elif currency4wg == "$CAD":
                            currency4wg = "CAD"
                        elif str([currency4wg])[4:-2] == "xa3":
                            currency4wg = "GBP"
                        elif str([currency4wg])[4:-2] == "u20ac":
                            currency4wg = "EUR"
                        elif str([currency4wg])[4:-2] == "xa5":
                            currency4b = "JPY"
                        #print k
                        #print currency4wg
                        #print weekendgross
                        #print date
                        #print screens


                        params = (pkno, title, k, currency4wg, weekendgross, date, screens)
                        cursor.execute("insert into boxoffice values (?, ?, ?, ?, ?, ?, ?)", params)
                        cnxn.commit()
                        print params
                        k += 1

    except BaseException, e:
        print line, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/release20000101_20141231/boxoffice_error_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/release20000101_20141231/boxoffice_error.txt", 'a')
        error_detail.write(line+'\n')
        error_detail.write(str(e)+'\n')
        error.write(line+'\n')
        error_detail.close()
        error.close()
f.close()
cnxn.close()
