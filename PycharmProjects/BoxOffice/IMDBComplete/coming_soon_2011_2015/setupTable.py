# -*- coding: utf-8 -*-
"""
Created on Thu Jan 08 15:26:31 2015

@author: BigData
"""
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
    

# -*- coding: utf-8 -*-
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cur = cnxn.cursor()
setup_table(cur)
cnxn.commit()
cnxn.close()
