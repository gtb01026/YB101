# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 16:53:41 2015

@author: BigData
"""
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
import shutil

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
cursor02 = cnxn.cursor()
cursor03 = cnxn.cursor()


#cursor.execute("SELECT b.currency4b, b.budget, ml.releasedate, b.pkno \
#                  FROM budget b, movie_list ml \
#                  WHERE b.pkno = ml.pkno AND b.currency4b != 'USD'")
cursor.execute("SELECT b.currency4b, b.budget, box.date, b.pkno \
                  FROM budget02 b, movie_list ml, boxoffice box \
                  WHERE b.pkno = box.pkno AND b.pkno = ml.pkno AND releasedate is not NULL AND box.weekend = '1' AND b.currency4b != 'USD'") 
row_coll = cursor.fetchall()
for row in row_coll:
#    print row
    if row[2] is not None:
        row[0] = str(row[0])
        row[1] = int(str(row[1]).split('L')[0])
        row[2] = str(row[2])
        print row
        cursor02.execute("SELECT " + row[0] + " \
              FROM historical_rate \
              WHERE date = ?", row[2])
        rate = cursor02.fetchone()
    #    rate = 1 / int(rate[0])
        if rate is not None:
            print rate[0]
            budget = int(row[1] / float(str(rate[0])))
            print budget
            print row[3]
            params = (budget, str(row[3]))            
            cursor03.execute("UPDATE budget02 \
                                SET currency4b = 'USD', budget = ? \
                                WHERE pkno = ?", params)
            cnxn.commit()
            
            
            
    else:
        print row
                      
    
#    
#    count03 = 0
#    for r in row:
#        file_dic[r[0].encode('utf-8')] = 1
#        if r[0].encode('utf-8') not in cast_dic:
#            print r[0].encode('utf-8')
#            count03 += 1



#country = f.readlines()[0].split(',')
#print country
#for line in f.readlines()[1:-8]:
#    params = line.split(',')
#    params[0] = params[0].replace('/', '-')
#    params[-1] = params[-1].split('\n')[0]
#    print params
#    cursor.execute("insert into historical_rate values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
#    cnxn.commit()
#    except BaseException, e:
#        print line, e
#        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_error_detail.txt", 'a')
#        error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_error.txt", 'a')
#        error_detail.write(line)
#        error_detail.write(str(e)+'\n')
#        error.write(line)
#        error_detail.close()
#        error.close()


cnxn.close()



