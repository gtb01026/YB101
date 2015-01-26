# -*- coding: utf-8 -*-
"""
Created on Wed Jan 07 12:29:47 2015

@author: BigData
"""
import requests
import urlparse 
from bs4 import BeautifulSoup 

bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/comingsoonafter20110101/comingsoonafter20110101.txt", 'w')
rs = requests.session()
#link_href = "http://www.imdb.com/movies-coming-soon/2011-01/"
page_format = "http://www.imdb.com/movies-coming-soon/%d"
for year in range(2010, 2016):
    page_format_year = page_format%(year) + "-"
    for month in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'):
        page = page_format_year + month
#        try:
        bid_list = rs.get(page)
        bid_response = bid_list.text.encode('utf8')
        bid_soup = BeautifulSoup(bid_response)
        img_primarys = bid_soup.select("#img_primary")
        for img_primary in img_primarys:
#            print img_primary
            movie_link = [tag['href'] for tag in img_primary.select('a')][0]
            movie_href = urlparse.urljoin("http://www.imdb.com/", movie_link)
            bid_file.write(str(year) + "-" + str(month) + "@" + movie_href + "\n")
        
        
#        except (KeyboardInterrupt, SystemExit):
#            rollback()
#            raise
#        except BaseException, e:
#            print link_href, e
#            error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/after20140701/get_movie_link_error_detail.txt", 'a')
#            error = open("C:/Users/BigData/Dropbox/BoxOffice/after20140701/get_movie_link_error.txt", 'a')
#            error_detail.write(link_href+'\n')
#            error_detail.write(str(e)+'\n')
#            error.write(link_href+'\n')
#            error_detail.close()
#            error.close()
#            rollback()
#        else:
#            commit()
            
bid_file.close()
    
    