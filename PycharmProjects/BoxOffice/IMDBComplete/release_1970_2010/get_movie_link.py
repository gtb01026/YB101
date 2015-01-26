# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 12:29:47 2015

@author: BigData
"""
import requests
import urlparse 
from bs4 import BeautifulSoup 

rs = requests.session()
link_href = "http://www.imdb.com/search/title?boxoffice_gross_us=10000,&release_date=1970-01-01,2010-12-31&runtime=60,"
bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/release1970_2010/1970_2010.txt", 'w')
page_dic = {}
while True:
    if link_href not in page_dic:
        page_dic[link_href] = 1
        try:
            bid_list = rs.get(link_href)
            bid_response = bid_list.text.encode('utf8')
            bid_soup = BeautifulSoup(bid_response)
            bid_table = bid_soup.select(".results")[0]
            bid_rows = bid_table.select("tr")[1:]
            count = 0
            for bid_row in bid_rows:
                movie_link = [tag['href'] for tag in bid_row.select('a')][0]
                movie_href = urlparse.urljoin("http://www.imdb.com/", movie_link)
                bid_file.write(movie_href + "\n")
            next_page = bid_soup.select(".pagination")[0]
            next_link = [tag['href'] for tag in next_page.select('a')][-1]
            link_href = urlparse.urljoin("http://www.imdb.com/", next_link)
        except BaseException, e:
            print link_href, e
            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/1970_2010/1970_2010_error_detail.txt", 'a')
            error = open("C:/Users/BigData/Dropbox/BoxOffice/1970_2010/1970_2010_error.txt", 'a')
            error_detail.write(link_href+'\n')
            error_detail.write(str(e)+'\n')
            error.write(link_href+'\n')
            error_detail.close()
            error.close()
    else:
        break
bid_file.close()
    
    
