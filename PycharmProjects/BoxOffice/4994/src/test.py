# -*- coding: utf-8 -*-
import pyodbc
import _uniout
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
print str(["À bout portant"])[2:-2]
d = str(["Rémy Girard"])[2:-2]

params = ("aa456123", d, "1", "aaa", "99999")
#print params
#cursor.execute("insert into casttest values (?, ?, ?, ?, ?)", params)
#cursor.execute("delete from directors where pkno = 'aa456123'")
#a = cursor.execute("SELECT title FROM casttest WHERE pkno = 'aa456123'")
#for b in a:
    #print eval('"'+b[0]+'"')

cnxn.commit()
cnxn.close()
#for b in a:
    #print b
#print str(a)#.encode('utf-8')
