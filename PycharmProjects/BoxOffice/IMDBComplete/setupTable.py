# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 15:26:31 2015

@author: BigData
"""
def setup_table(cur):
#    cur.execute('''CREATE TABLE budget(
#        pkno nvarchar(100),
#        title nvarchar(100),
#        currency4b nvarchar(100),
#        budget bigint,
#        )''')
    cur.execute('''CREATE TABLE boxoffice02(
         pkno nvarchar(100),
         title nvarchar(100),
         weekend int,
         currency4wg nvarchar(100),
         weekendgross bigint,
         date date,
         screens bigint,
         )''')
#    cur.execute('''CREATE TABLE cast(
#         pkno nvarchar(100),
#         title nvarchar(100),
#         priority4c int,
#         cano nvarchar(100),
#         cast nvarchar(100),
#         )''')
#    cur.execute('''CREATE TABLE combine(
#         pkno nvarchar(100),
#         title nvarchar(100),
#         type4t nvarchar(100),
#         priority4t int,
#         cano nvarchar(100),
#         temp nvarchar(100),
#         )''')         
#    cur.execute('''CREATE TABLE movie_list(
#        pkno nvarchar(100),
#        title nvarchar(100),
#        topdirector nvarchar(100),
#        topwriterorproducer nvarchar(100),
#        topgenres nvarchar(100),
#        currency4b nvarchar(100),
#        budget bigint,
#        releasedate date,
#        openingweekend_date date,
#        currency4owg nvarchar(100),
#        openingweekend_gross bigint,
#        openingweekend_screens int,
#        lastweekend_date date,
#        totalgross bigint,
#        totalscreens bigint,
#        totalweekend int,
#        image_link4movie nvarchar(200),
#        predictclass int,
#        predictstars nvarchar(100),
#        predict4owg bigint,
#        predict4owg_lowerbound bigint,
#        predict4owg_upperbound bigint,
#        )''')
#    cur.execute('''CREATE TABLE genres(
#         pkno nvarchar(100),
#         title nvarchar(100),
#         priority4g int,
#         genre nvarchar(100),
#         )''')
#    cur.execute('''CREATE TABLE historical_rate(
#         date date,
#         ARS float,
#         AUD float,
#         BEF float,
#         BRL float,
#         CAD float,
#         CHF float,
#         CNY float,
#         CZK float,
#         DEM float,
#         DKK float,
#         ESP float,
#         EUR float,
#         FRF float,
#         FIM float,
#         GBP float,
#         HKD float,
#         HUF float,
#         IEP float,
#         INR float,
#         ISK float,
#         ITL float,
#         JMD float,
#         JPY float,
#         KRW float,
#         MXN float,
#         NOK float,
#         NZD float,
#         PLN float,
#         SEK float,
#         SGD float,
#         THB float,
#         USD float,
#         VEB float,
#         )''')
#    cur.execute('''CREATE TABLE historical_rate02(
#         date date,
#         type nvarchar(100)
#         rate float,
#         )''')   
#     cur.execute('''CREATE TABLE locations(
#                 pkno nvarchar(100),
#                 title nvarchar(100),
#                 country nvarchar(100),
#                 state nvarchar(100),
#                 city nvarchar(100),
#                 location nvarchar(200),
#                 numerator int,
#                 denominator int,
#                 fraction float,
#                 )''')
#     cur.execute('''CREATE TABLE genres_order_by_totalgross(
#                 genre nvarchar(100),
#                 genre_order_by_totalgross int,
#                 )''')
#     cur.execute('''CREATE TABLE awards(
#                 cano nvarchar(100),
#                 award nvarchar(100),
#                 award_category nvarchar(100),
#                 award_year int,
#                 award_outcome nvarchar(100),
#                 award_description nvarchar(100),
#                 award_movie nvarchar(100),
#                 pkno nvarchar(100),
#                 award_movie_year int,
#                 )''')
    # cur.execute('''CREATE TABLE movie_image(
    #             pkno nvarchar(100),
    #             image4movie image,
    #             )''')
    # cur.execute('''CREATE TABLE movie_image_link(
    #             pkno nvarchar(100),
    #             image_link4movie nvarchar(200),
    #             )''')

    

# -*- coding: utf-8 -*-
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cur = cnxn.cursor()
setup_table(cur)
cnxn.commit()
cnxn.close()
