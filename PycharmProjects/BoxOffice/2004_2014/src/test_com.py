# -*- coding: utf-8 -*-
import pyodbc
import _uniout
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
#print str(["bout portant"])[2:-2]
#d = str(["À bout portant"])[2:-2]
#print type("Rémy Girard")
d = "Rémy Girard".decode('utf-8')
#d = "Rémy Girard"
print type(d)
#print str(["£"])[2:-2]
e = str(["£"])[2:-2]
params = ("tt456123", d, "1", "fff", "99999")
#print params
#cursor.execute("insert into boxoffice_com values (?, ?, ?, ?, ?)", params)
cursor.execute("insert into casttest values (?, ?, ?, ?, ?)", params)
#cursor.execute("delete from  where pkno = 'aa456123'")
a = cursor.execute("SELECT title FROM casttest WHERE pkno = 'tt456123'")
for b in a:
    print b[0]
    print eval('"'+b[0]+'"')

cnxn.commit()
cnxn.close()
#for b in a:
    #print b
#print str(a)#.encode('utf-8')
