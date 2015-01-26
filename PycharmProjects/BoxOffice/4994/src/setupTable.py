def setup_table(cur):
    cur.execute('''CREATE TABLE movie_list(
                pkno nvarchar(100),
                title nvarchar(100),
                currency4b nvarchar(100),
                budget bigint,
                openingweekend_date date,
                currency4owg nvarchar(100),
                openingweekend_gross bigint,
                openingweekend_screens int,
                totalgross bigint,
                totalscreens bigint,
                totalweekend int,
                image_link4movie nvarchar(200),
                )''')
    # cur.execute('''CREATE TABLE title_decode(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             )''')
    # cur.execute('''CREATE TABLE locations_de(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             country nvarchar(100),
    #             state nvarchar(100),
    #             city nvarchar(100),
    #             location nvarchar(200),
    #             numerator int,
    #             denominator int,
    #             fraction float,
    #             )''')
    # cur.execute('''CREATE TABLE awards3(
    #             cano nvarchar(100),
    #             award nvarchar(100),
    #             award_category nvarchar(100),
    #             award_year int,
    #             award_outcome nvarchar(100),
    #             award_description nvarchar(100),
    #             award_movie nvarchar(100),
    #             pkno nvarchar(100),
    #             award_movie_year int,
    #             )''')
    # cur.execute('''CREATE TABLE cast(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             priprity4c int,
    #             cano nvarchar(100),
    #             cast nvarchar(100),
    #             )''')
    # cur.execute('''CREATE TABLE combine_cano(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             type4t nvarchar(100),
    #             priority4t int,
    #             cano nvarchar(100),
    #             temp nvarchar(100),
    #             )''')
    # cur.execute('''CREATE TABLE movie_image(
    #             pkno nvarchar(100),
    #             image4movie image,
    #             )''')
    # cur.execute('''CREATE TABLE movie_image_link(
    #             pkno nvarchar(100),
    #             image_link4movie nvarchar(200),
    #             )''')

# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cur = cnxn.cursor()
#path = "C:/Users/BigData/BoxOffice/bid_detail/2000/"
#dirs = os.listdir( path )
setup_table(cur)
#for filename in dirs:
    #print filename
    #soup = get_soup(path + filename)
    #print soup
    #directors_info_dic = get_directors_info_dic(soup)
    #tenderer_info_dic = get_tenderer_info_dic(soup)
    #tender_award_item_dic = get_tender_award_item_dic(soup)

    #insert_directors_info(cur, directors_info_dic, filename)
    #insert_tenderer_info(cur, tenderer_info_dic, filename, tenderer_sql)
    #insert_tenderawarditem_info(cur, tender_award_item_dic, filename, tenderawarditem_sql)

cnxn.commit()
cnxn.close()