# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
        
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()

path = "C:/Users/BigData/Dropbox/BoxOffice/bid_list/"
filenames = os.listdir(path)
for filename in filenames:
    f = open(path + filename, "r")
    for line in f.readlines():
        try:
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
            for part in "".join(table.text).split("\n\n"):
                ele2 = part.split("\n")[0]
                if ele2 == "Weekend Gross":
                    aaa = part.split("\n")[1].split(")")
                    i = 0
                    aspl_dic = {}
                    for a in aaa:
                        aspl_dic[i] = a.split(" (")
                        i += 1

                    wg_dic = {}
                    k = 1
                    for j in range(len(aspl_dic)-2, -1, -1):
                        if aspl_dic[j][1] == "USA":
                            #print len(aspl_dic[j+2])
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
                            m = re.match(r"([^0-9]+)([0-9,]+)",aspl_dic[j][0])
                            currency4wg = m.groups()[0].strip()
                            weekendgross = m.groups()[1].strip().replace(",", "")
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

                            if currency4wg == "$":
                                currency4wg = "USD"
                            if str([currency4wg])[4:-2] == "$CAD":
                                currency4wg = "CAD"
                            elif str([currency4wg])[4:-2] == "xa3":
                                currency4wg = "GBP"
                            elif str([currency4wg])[4:-2] == "u20ac":
                                currency4wg = "EUR"
                            elif str([currency4wg])[4:-2] == "xa5":
                                currency4wg = "JPY"

                            params = (pkno, title_code, k, currency4wg, weekendgross, date, screens)
                            cursor.execute("insert into boxoffice values (?, ?, ?, ?, ?, ?, ?)", params)
                            cnxn.commit()
                            print params
                            k += 1

        except BaseException, e:
            print line, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/boxofficeCom_error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list_error/boxofficeCom_error.txt", 'a')
            error_detail.write(line)
            error_detail.write(str(e))
            error.write(line)
            error_detail.close()
            error.close()
    f.close()
cnxn.close()