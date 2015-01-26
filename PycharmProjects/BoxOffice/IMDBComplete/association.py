# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 12:11:49 2015

@author: BigData
"""
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
cursor02 = cnxn.cursor()
cursor03 = cnxn.cursor()
cursor.execute("SELECT cano \
                FROM cast \
                GROUP BY cano \
                HAVING count(title) > 1")
cano_coll = cursor.fetchall()
cano_dic = {}
for cano in cano_coll:
    cano_dic[cano[0]] = 1

cursor02.execute("SELECT pkno \
                  FROM cast \
                  WHERE cano in (SELECT cano \
    					FROM cast \
    					GROUP BY cano \
    					HAVING count(title) > 1) \
                  GROUP BY pkno")
pkno_coll = cursor02.fetchall()
#print pkno_coll
for pkno in pkno_coll:
    cursor03.execute("SELECT cano \
                        FROM cast \
                        WHERE pkno = ? \
                        ORDER BY cano ", pkno[0])
    cano_coll03 = cursor03.fetchall()
    print pkno[0]
    bid_file = open("C:/Users/BigData/Desktop/association02.txt", 'a')
    bid_file.write(pkno[0])
    for cano03 in cano_coll03:
        if cano03[0] in cano_dic:
            print cano03[0]
            bid_file.write(','+cano03[0])
        
    bid_file.write('\n')
    bid_file.close()
    
    
cnxn.close()
