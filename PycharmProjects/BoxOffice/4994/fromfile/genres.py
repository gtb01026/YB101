cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=IMDB')
cursor = cnxn.cursor()
path = "C:/Users/BigData/BoxOffice/movie_detail/" 
dirs = os.listdir( path ) 
#setup_table(cur)
count = 1
for filename in dirs:
    #print filename
    soup = get_soup(path + filename) 
    #print soup
    pkno = filename.split(".txt")[0]
    #print pkno
    top = soup.select('.maindetails_center')[0]
    itemprop = top.select('.itemprop')[0].text.encode('utf-8')
    title = " ".join(itemprop.split())
    #print title
        
    a = soup.select('#title-overview-widget-layout')[0]
    #print a
    b = a.select('.txt-block')
    #print b
    for c in b:
        #print c
        d = c.select('.inline')
        #print d
        for e in d:
            #print e.text.split()[0]
            #print e.split("\n")[1].split(" ")[-1]
            if e.text.split()[0] == "Director:" or e.text.split()[0] == "Directors:":
                #print c
                f = c.select('.itemprop')
                for g in f:
                    print pkno
                    print title
                    print " ".join(g.text.split())
                    params = (count, pkno, title, " ".join(g.text.split()))
                    cursor.execute("insert into directors values (?, ?, ?, ?)", params)
                    cnxn.commit()
                    count += 1
                    
                              
    
cnxn.close()