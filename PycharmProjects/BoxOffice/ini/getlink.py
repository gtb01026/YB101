import requests
import urlparse 
from bs4 import BeautifulSoup 
from math import ceil

rs = requests.session()
page_format = "http://www.imdb.com/year/%d"
for page in range(2014, 2015):
    try:
        ini = rs.get(page_format%(page))
        ini_text = ini.text.encode('utf8')
        ini_soup = BeautifulSoup(ini_text)
        ini_link = ini_soup.select(".see-more")[0]
        link = [tag['href'] for tag in ini_link.select('a')][0]
        link_href = urlparse.urljoin("http://www.imdb.com/", link)
        bid_file = open("C:/Users/BigData/Dropbox/BoxOffice/bid_list/%s_2.txt"%(page), 'w')
        page_dic = {}
        while True:
            if link_href not in page_dic:
                page_dic[link_href] = 1
                bid_list = rs.get(link_href)
                bid_response = bid_list.text.encode('utf8')
                bid_soup = BeautifulSoup(bid_response)
                bid_table = bid_soup.select(".results")[0]
                bid_rows = bid_table.select("tr")[1:]
                #print bid_rows
                count = 0
                for bid_row in bid_rows:
                    movie_link = [tag['href'] for tag in bid_row.select('a')][0]
                    movie_href = urlparse.urljoin("http://www.imdb.com/", movie_link)
                    bid_file.write(movie_href + "\n")
                    #print movie_href
                    #count += 1
                #print count
                #print link_href
                next_page = bid_soup.select(".pagination")[0]
                next_link = [tag['href'] for tag in next_page.select('a')][-1]
                link_href = urlparse.urljoin("http://www.imdb.com/", next_link)

            else:
                break

        bid_file.close()
    except BaseException, e:
        print link_href, e
        error_detail = open("C:/Users/BigData/Dropbox/BoxOffice/get2014linkerror_detail.txt", 'a')
        error = open("C:/Users/BigData/Dropbox/BoxOffice/get2014linkerror.txt", 'a')
        error_detail.write(link_href+'\n')
        error_detail.write(str(e)+'\n')
        error.write(link_href+'\n')
        error_detail.close()
        error.close()