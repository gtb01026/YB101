# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 12:29:47 2015

@author: BigData
"""
import requests
import urlparse 
from bs4 import BeautifulSoup 
import re

datenlink_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_date.txt", 'w')
link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015.txt", 'w')
rs = requests.session()
#link_href = "http://www.imdb.com/movies-coming-soon/2011-01/"
page_format = "http://www.imdb.com/movies-coming-soon/%d"
for year in range(2011, 2016):
    page_format_year = page_format%(year) + "-"
    for month in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'):
        page = page_format_year + month
        try:
            bid_list = rs.get(page)
            bid_response = bid_list.text.encode('utf8')
            bid_soup = BeautifulSoup(bid_response)
            main = bid_soup.select("#main")[0]
    #        print main
            list_detail = main.select("div")[6]
    #        print list_detail
            a_coll = list_detail.select("a")
            for a in a_coll:
    #            print a
    #            time.sleep(1)
                if a.text.split() is not None and len(a.text.split()) == 2:
                    try:
                        if a.text.split()[0] in ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December') and int(a.text.split()[1]) in range(1, 31):
                            day = str(a.text.split()[1])
                            if len(day) == 1:
                                day = "0" + day
                    except ValueError, e:
                        print e
    #        if a['href']:            
                try:
                    movie_link = a['href']
    #                print movie_link
                    n = re.match(r'/title/tt[0-9]+/\?ref_=cs_ov_([a-z]+)', movie_link)
                    if n is not None:
                        if n.group(1) == 'tt':
                            movie_href = urlparse.urljoin("http://www.imdb.com/", movie_link)
                            print movie_href
                            line = str(year) + "-" + str(month) + "-" + day + "@" + movie_href
                            link_file.write(movie_href + "\n")
                            datenlink_file.write(line + "\n")
                except KeyError, e:
                    print e
            
    #        
        
        except BaseException, e:
            print page, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/get_movie_link_error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/get_movie_link_error.txt", 'a')
            error_detail.write(page+'\n')
            error_detail.write(str(e)+'\n')
            error.write(page+'\n')
            error_detail.close()
            error.close()
            
link_file.close()            
datenlink_file.close()
    
    