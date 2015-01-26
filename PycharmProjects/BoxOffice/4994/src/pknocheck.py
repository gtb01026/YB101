#%%
cast_dic = {}
file_dic = {}
match_dic = {}
#%%
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/1970_2010.txt", "r")
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/release1970_2010-comingsoonafter2011_2015", 'w')
count = 0
for line in f.readlines(): 
    link = line.strip()
    pkno = link.split('/')[4]
    file_dic[pkno] = 1
    if pkno not in cast_dic:
#        link_file.write(line)
        match_dic[pkno] = 1
        count += 1

#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_02.txt", "r")
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015-release1970_2010.txt", 'w')
count02 = 0
for line in f.readlines(): 
    link = line.strip()
    pkno = link.split('/')[4]
    cast_dic[pkno] = 1
    if pkno in file_dic:
#        link_file.write(line)
        match_dic[pkno] = 1
        count02 += 1
        
#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
#去除comingsoon重複
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_date.txt", "r")
#datenlink_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_date_02.txt", 'w')
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_02.txt", 'w')
count02 = 0
for line in f.readlines(): 
    link = line.split('@')[1]
    pkno = link.split('/')[4]
    if pkno  not in cast_dic:
        cast_dic[pkno] = 1
#        datenlink_file.write(line)
#        link_file.write(link)
    elif pkno in cast_dic:
        match_dic[pkno] = 1
#        match_dic[pkno] = 1
        count02 += 1
        
#datenlink_file.close()          
#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
cursor.execute("SELECT DISTINCT pkno FROM genres")
row = cursor.fetchall()
cast_dic = {}
if row:
    for r in row:
        #print r[0]
        cast_dic[r[0]] = 1
        if r[0] not in file_dic:
            print r[0]

cnxn.close()