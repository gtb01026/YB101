# -*- coding: utf-8 -*-
"""
Created on Fri Jan 09 20:04:42 2015

@author: BigData
"""
#%%
cast_dic = {}
file_dic = {}
match_dic = {}
#%%
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/temp.txt", "r")
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/release1970_2010-comingsoonafter2011_2015", 'w')
count = 0
for line in f.readlines(): 
    link = line.strip()
    pkno = link.split('/')[4]
#    pkno = link.split('/')[-1].split('?')[0]
    file_dic[pkno] = 1
    if pkno not in cast_dic:
#        file_dic[pkno] = 1
        match_dic[pkno] = 1
#    else:
#        print pkno
##        link_file.write(line)
#        match_dic[pkno] = 1
#        count += 1

#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/release1970_2010/movie_img_link.txt", "r")
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015-release1970_2010.txt", 'w')
count02 = 0
for line in f.readlines(): 
    link = line.strip()
#    pkno = link.split('/')[4]
    pkno = link.split('/')[-1].split('?')[0]
    cast_dic[pkno] = 1
#    if pkno not in file_dic:
#        link_file.write(line)
#        match_dic[pkno] = 1
#        count02 += 1
        
#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
# -*- coding: utf-8 -*-
for pkno in match_dic: 
    if pkno not in cast_dic:
        print pkno
#        link_file.write(line)
#        match_dic[pkno] = 1
#        count02 += 1
        
#link_file.close()          
f.close()

print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
#%%
#去除comingsoon重複
# -*- coding: utf-8 -*-
f = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/movie_img_link.txt", "r")
#datenlink_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_date_02.txt", 'w')
#link_file = open("C:/Users/BigData/Dropbox/BoxOffice/IMDBComplete/comingsoonafter2011_2015/comingsoonafter2011_2015_02.txt", 'w')
count02 = 0
for line in f.readlines(): 
#    link = line.split('@')[1]
#    pkno = link.split('/')[4]
    pkno = link.split('/')[-1].split('?')[0]
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
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDBComplete')
cursor = cnxn.cursor()
cursor.execute("SELECT [pkno] \
                FROM [IMDBComplete].[dbo].[movie_list] \
                WHERE [image_link4movie] is not NULL")
row = cursor.fetchall()
if row:
    count03 = 0
    for r in row:
        file_dic[r[0].encode('utf-8')] = 1
        if r[0].encode('utf-8') not in cast_dic:
            print r[0].encode('utf-8')
            count03 += 1

cnxn.close()
