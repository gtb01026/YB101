# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
#f = open("C:/Users/BigData/Dropbox/BoxOffice/4994.txt", "r")
cursor.execute("SELECT DISTINCT cano FROM castncrew_list ORDER BY cano")
cano_coll = cursor.fetchall()
for cano in cano_coll:
#    print type(cano)
    print cano
#    try:
#        rs = requests.session()
#        request_get = requests.get("http://www.imdb.com/name/" + cano[0] + "/awards?ref_=nm_ql_2")
#        #request_get = requests.get("http://www.imdb.com/name/nm0000111/awards?ref_=nm_ql_2")
#        # print request_get
#        response = request_get.text.encode('utf8')
#        soup = BeautifulSoup(response)
#        main = soup.select('#main')[0]
#        #print main.text.strip()
#        h3_coll = main.select('h3')[1:]
#        table_coll = main.select('table')
#        count = 0
#        for h3 in h3_coll:
#            award =  h3.text
#            tr_coll = table_coll[count].select('tr')
#            for tr in tr_coll:
#                td_coll = tr.select('td')
#                #print len(td_coll)
#                if len(td_coll) == 3:
#                    award_category = td_coll[1].select('span')[0].text
#                    #print award
#                    award_year = td_coll[0].text.split()[0]
#                    award_outcome = td_coll[1].text.split()[0]
#                    try:
#                        award_description = ' '.join(td_coll[2].text.split('\n')[1].split())
#                        if award_description == '':
#                            award_description = "99999"
#                    except IndexError, e:
#                        award_description = "99999"
#                    try:
#                        award_movie = td_coll[2].select('a')[0].text
#                        award_movie_year = td_coll[2].select('span')[0].text.split('(')[1].split(')')[0]
#                        #print td_coll[2].select('a')
#                        title_link = [tag['href'] for tag in td_coll[2].select('a')][0]
#                        pkno = title_link.split('/')[2].split('?')[0]
#                        #print type(str(pkno.decode('utf-8')))
#                        n = re.match(r'([a-z]{2})[0-9]+', str(pkno.decode('utf-8')))
#                        if n.group(1) != 'tt':
#                            award_movie = "99999"
#                            award_movie_year = "99999"
#                            pkno = "99999"
#                    except IndexError, e:
#                        award_movie = "99999"
#                        award_movie_year = "99999"
#                        pkno = "99999"
#                    # print award
#                    # print award_category
#                    # print award_year
#                    # print award_outcome
#                    # print award_description
#                    # print award_movie
#                    # print pkno
#                    # print award_movie_year
#                    # print "~~~~~~~~~~~~~~~~~~~~~"
#
#                if len(td_coll) == 2:
#                    award_category = td_coll[0].select('span')[0].text
#                    award_outcome = td_coll[0].text.split()[0]
#                    try:
#                        award_description = ' '.join(td_coll[1].text.split('\n')[1].split())
#                        if award_description == '':
#                            award_description = "99999"
#                    except IndexError, e:
#                        award_description = "99999"
#                    try:
#                        award_movie = td_coll[1].select('a')[0].text
#                        award_movie_year = td_coll[1].select('span')[0].text.split('(')[1].split(')')[0]
#                        #print td_coll[0].select('a')
#                        title_link = [tag['href'] for tag in td_coll[1].select('a')][0]
#                        pkno = title_link.split('/')[2].split('?')[0]
#                        n = re.match(r'([a-z]{2})[0-9]+', str(pkno.decode('utf-8')))
#                        if n.group(1) == 'nm':
#                            award_movie = "99999"
#                            award_movie_year = "99999"
#                            pkno = "99999"
#                    except IndexError, e:
#                        award_movie = "99999"
#                        award_movie_year = "99999"
#                        pkno = "99999"
#                    # print award
#                    # print award_category
#                    # print award_year
#                    # print award_outcome
#                    # print award_description
#                    # print award_movie
#                    # print pkno
#                    # print award_movie_year
#                    # print "~~~~~~~~~~~~~~~~~~~~~"
#
#                #print len(td_coll)
#                if len(td_coll) == 1:
#                    try:
#                        award_description = ' '.join(td_coll[0].text.split('\n')[1].split())
#                        if award_description == '':
#                            award_description = "99999"
#                    except IndexError, e:
#                        award_description = "99999"
#                    try:
#                        award_movie = td_coll[0].select('a')[0].text
#                        award_movie_year = td_coll[0].select('span')[0].text.split('(')[1].split(')')[0]
#                        #print td_coll[0].select('a')
#                        title_link = [tag['href'] for tag in td_coll[0].select('a')][0]
#                        pkno = title_link.split('/')[2].split('?')[0]
#                        n = re.match(r'([a-z]{2})[0-9]+', str(pkno.decode('utf-8')))
#                        if n.group(1) == 'nm':
#                            award_movie = "99999"
#                            award_movie_year = "99999"
#                            pkno = "99999"
#                    except IndexError, e:
#                        award_movie = "99999"
#                        award_movie_year = "99999"
#                        pkno = "99999"
#                    # print award
#                    # print award_category
#                    # print award_year
#                    # print award_outcome
#                    # print award_description
#                    # print award_movie
#                    # print pkno
#                    # print award_movie_year
#                    # print "~~~~~~~~~~~~~~~~~~~~~"
#                params = (cano[0], award, award_category, award_year, award_outcome, award_description, award_movie, pkno, award_movie_year)
#                # cursor.execute("insert into awards values (?, ?, ?, ?, ?, ?, ?, ?, ?)", params)
#                # cnxn.commit()
#                # print params
#            count += 1
#
#
#    except BaseException, e:
#        print cano, e
#        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/.txt", 'a')
#        error = open("C:/Users/BigData/Dropbox/BoxOffice/.txt", 'a')
#        error_detail.write(cano[0]+'\n')
#        error_detail.write(str(e)+'\n')
#        error.write(cano[0]+'\n')
#        error_detail.close()
#        error.close()


cnxn.close()
