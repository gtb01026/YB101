# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
import shutil

f= open('img_link_list.txt','w')
res = requests.get('http://dnameth.pixnet.net/album/set/13547803-%E6%B5%B7%E8%B3%8A%E7%8E%8B-%E5%BD%A9%E5%9C%96')
response = res.text.encode('utf-8')
soup = BeautifulSoup(response)
table = soup.find('ul',{'class':'photo-grid-list'})
#print table
rows = table.findAll('li',{'class':'photo-grid'})
#print rows
for row in rows: 

    links = [tag['href']for tag in row.select('a')] [0]
    
    f.write(links+"\n")


    print links
f.close()

#這以上抓連結 以下是抓圖

img_list = open('img_link_list.txt','r')
for line in img_list.readlines():
    imglink = line.strip()
    res1 = requests.get(imglink)
    response1 = res1.text.encode('utf-8')
    #print response1
    soup1 = BeautifulSoup(response1)
    table1 = soup1.find('div',{'class':'item-frame item-photo-frame'})
    #print table1
    rows1 = table1.select('a')[0]
    #print rows1
    row1 = rows1.find('img')
    row2 = row1['src']
    #print row2
    row3 = row2.split('/')[-1] #取得最後一個斜線後面的字串
    print row3
    rs = requests.get(row2,stream=True)
    with open('%s'%(row3),'wb')as out_file: #檔名一定要用這樣的格式替換
        shutil.copyfileobj(rs.raw,out_file)
        del rs
img_list.close() 