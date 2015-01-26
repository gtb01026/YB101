# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc, time

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
request_get = requests.get("http://www.imdb.com/name/nm0000136/awards?ref_=nm_ql_2")
# print request_get
response = request_get.text.encode('utf8')
soup = BeautifulSoup(response)
main = soup.select('#main')[0]
#print main.text.strip()
h3_coll = main.select('h3')
table_coll = main.select('table')
count = -1
for h3 in h3_coll:
    print h3.text
    if h3.text == "Academy Awards, USA":
        #award = "Oscar"
        tr_coll = table_coll[count].select('tr')
        for tr in tr_coll:
            td_coll = tr.select('td')
            #print len(td_coll)
            if len(td_coll) == 3:
                award = td_coll[1].select('span')[0].text
                award_year = td_coll[0].text.split()[0]
                award_outcome = td_coll[1].text.split()[0]
                award_movie = td_coll[2].select('a')[0].text
                award_movie_year = td_coll[2].select('span')[0].text
                #print td_coll[2].select('a')
                title_link = [tag['href'] for tag in td_coll[2].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"

            #print len(td_coll)
            if len(td_coll) == 1:
                award_movie = td_coll[0].select('a')[0].text
                award_movie_year = td_coll[0].select('span')[0].text
                #print td_coll[0].select('a')
                title_link = [tag['href'] for tag in td_coll[0].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"

    if h3.text == "Golden Globes, USA":
        #award = "Golden Globe"
        tr_coll = table_coll[count].select('tr')
        for tr in tr_coll:
            td_coll = tr.select('td')
            #print len(td_coll)
            if len(td_coll) == 3:
                award = td_coll[1].select('span')[0].text
                award_year = td_coll[0].text.split()[0]
                award_outcome = td_coll[1].text.split()[0]
                award_movie = td_coll[2].select('a')[0].text
                award_movie_year = td_coll[2].select('span')[0].text
                #print td_coll[2].select('a')
                title_link = [tag['href'] for tag in td_coll[2].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"

            #print len(td_coll)
            if len(td_coll) == 1:
                award_movie = td_coll[0].select('a')[0].text
                award_movie_year = td_coll[0].select('span')[0].text
                #print td_coll[0].select('a')
                title_link = [tag['href'] for tag in td_coll[0].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"

    if h3.text == "BAFTA Awards":
        #award = "Golden Globe"
        tr_coll = table_coll[count].select('tr')
        for tr in tr_coll:
            td_coll = tr.select('td')
            #print len(td_coll)
            if len(td_coll) == 3:
                award = td_coll[1].select('span')[0].text
                award_year = td_coll[0].text.split()[0]
                award_outcome = td_coll[1].text.split()[0]
                award_movie = td_coll[2].select('a')[0].text
                award_movie_year = td_coll[2].select('span')[0].text
                #print td_coll[2].select('a')
                title_link = [tag['href'] for tag in td_coll[2].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"

            #print len(td_coll)
            if len(td_coll) == 1:
                award_movie = td_coll[0].select('a')[0].text
                award_movie_year = td_coll[0].select('span')[0].text
                #print td_coll[0].select('a')
                title_link = [tag['href'] for tag in td_coll[0].select('a')][0]
                pkno = title_link.split('/')[2].split('?')[0]
                print award
                print award_year
                print award_outcome
                print award_movie
                print pkno
                print award_movie_year
                print "~~~~~~~~~~~~~~~~~~~~~"




    count += 1