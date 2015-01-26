def setup_table(cur):
    # cur.execute('''CREATE TABLE cast(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             priprity4c int,
    #             cast nvarchar(100),
    #             volume bigint,
    #             )''')
    # cur.execute('''CREATE TABLE budget(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             currency4b nvarchar(100),
    #             budget bigint,
    #             yearinimdb int,
    #             )''')
    # cur.execute('''CREATE TABLE boxoffice(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             weekend int,
    #             currency4wg nvarchar(100),
    #             weekendgross int,
    #             date date,
    #             screens int,
    #             )''')
    # cur.execute('''CREATE TABLE combine(
    #             pkno nvarchar(100),
    #             title nvarchar(100),
    #             type4t nvarchar(100),
    #             priority4t int,
    #             temp nvarchar(100),
    #             )''')
    cur.execute('''CREATE TABLE genres(
                pkno nvarchar(100),
                title nvarchar(100),
                priority4g int,
                genre nvarchar(100),
                )''')

# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from datetime import datetime
import os, sys, re
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
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