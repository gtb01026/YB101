import requests
import urlparse
from bs4 import BeautifulSoup
from math import ceil
f = open("C:/Users/BigData/Dropbox/BoxOffice/4994.txt", "r")
for line in f.readlines():
    rec = line.strip().split("\n")
    for link in rec:
        try:
            pkno = link.split('/')[4]
            rs = requests.session()
            # bid_detail = open("C:/Users/BigData/BoxOffice/bid_detail/2007/" + pkno + ".txt", 'w')
            # request_get = requests.get("http://www.imdb.com/title/" + pkno + "/")
            # response = request_get.text.encode('utf8')
            # soup = BeautifulSoup(response)
            # printarea = soup.select('#pagecontent')[0]
            # bid_detail.write(printarea.prettify("utf-8"))
            # bid_detail.close()
            # print pkno
            # bid_detail = open("C:/Users/BigData/BoxOffice/boxoffice/" + pkno + ".txt", 'w')
            # request_get = requests.get("http://www.imdb.com/title/" + pkno + "/business?ref_=tt_dt_bus")
            # response = request_get.text.encode('utf8')
            # soup = BeautifulSoup(response)
            # printarea = soup.select('#tn15content')[0]
            # bid_detail.write(printarea.prettify("utf-8"))
            # bid_detail.close()
            # print pkno
            bid_detail = open("C:/Users/BigData/Dropbox/BoxOffice/castncrew_detail/" + pkno + ".txt", 'w')
            request_get = requests.get("http://www.imdb.com/title/" + pkno + "/fullcredits?ref_=tt_ov_st_sm")
            response = request_get.text.encode('utf8')
            soup = BeautifulSoup(response)
            printarea = soup.select('#main')[0]
            bid_detail.write(printarea.prettify("utf-8"))
            bid_detail.close()
            print pkno
        except BaseException, e:
            print line, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/getlink_error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/getlink_error.txt", 'a')
            error_detail.write(line)
            error_detail.write(str(e))
            error.write(line)
            error_detail.close()
            error.close()
f.close()