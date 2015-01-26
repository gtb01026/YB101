# -*- coding: utf-8 -*-
import requests
import urlparse
from bs4 import BeautifulSoup
from math import ceil

f = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list/2014.txt", "r")
#f = open("C:/Users/BigData/Dropbox/BoxOffice/getlink2007_error.txt", "r")
for line in f.readlines():
    rec = line.strip().split("\n")
    for link in rec:
        try:
            pkno = link.split('/')[4]
            rs = requests.session()
            # bid_detail = open("C:/Users/BigData/Dropbox/BoxOffice/bid_detail/2007/" + pkno + ".txt", 'w')
            # request_get = requests.get("http://www.imdb.com/title/" + pkno + "/")
            # response = request_get.text.encode('utf8')
            # soup = BeautifulSoup(response)
            # printarea = soup.select('#pagecontent')[0]
            # bid_detail.write(printarea.prettify("utf-8"))
            # bid_detail.close()
            # print pkno

            bid_detail = open("C:/Users/BigData/Dropbox/BoxOffice/box_detail/2014/" + pkno + ".txt", 'w')
            request_get = requests.get("http://www.imdb.com/title/" + pkno + "/business?ref_=tt_dt_bus")
            response = request_get.text.encode('utf8')
            soup = BeautifulSoup(response)
            printarea = soup.select('#tn15content')[0]
            bid_detail.write(printarea.prettify("utf-8"))
            bid_detail.close()
            print pkno
        except BaseException, e:
            print line, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/box_detail_error/box2014error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/box_detail_error/box2014error.txt", 'a')
            error_detail.write(line)
            error_detail.write(str(e))
            error.write(line)
            error_detail.close()
            error.close()

        try:
            bid_detail = open("C:/Users/BigData/Dropbox/BoxOffice/crew_detail/2014/" + pkno + ".txt", 'w')
            request_get = requests.get("http://www.imdb.com/title/" + pkno + "/fullcredits?ref_=tt_ov_st_sm")
            response = request_get.text.encode('utf8')
            soup = BeautifulSoup(response)
            printarea = soup.select('#main')[0]
            bid_detail.write(printarea.prettify("utf-8"))
            bid_detail.close()
            print pkno
        except BaseException, e:
            print line, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/crew_detail_error/crew2014error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/crew_detail_error/crew2014error.txt", 'a')
            error_detail.write(line)
            error_detail.write(str(e))
            error.write(line)
            error_detail.close()
            error.close()
f.close()