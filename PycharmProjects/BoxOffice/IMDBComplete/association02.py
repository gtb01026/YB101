# -*- coding: utf-8 -*-
"""
Created on Wed Jan 14 19:35:34 2015

@author: BigData
"""
#%%
bi_dic = {}
#%%
from itertools import chain, combinations

def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable( combinations(xs,n) for n in range(2,3) )

f = open("C:/Users/BigData/Desktop/aaa.txt", 'r')
for line in f.readlines():
    line = line.split('\n')[0]
    s = list(powerset(set(line.split(',')[1:])))
#    print s
    for bi in s:
        bi = tuple(sorted(bi))
        print ''.join(bi)
#        if bi not in bi_dic:
#            bi_dic[bi] = 1
#        else:
#            bi_dic[bi] += 1
#print bi_dic
f.close()
#%%
from itertools import chain, combinations
import sys 

def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable( combinations(xs,n) for n in range(2,3) )
  
for line in sys.stdin:
    line = line.split('\n')[0]
    s = list(powerset(set(line.split(',')[1:])))
#    print s
    for bi in s:
        bi = tuple(sorted(bi))
        print '%s\t%s' % (bi, 1)
#%%
import sys

current_bi = None
current_count = 0
bi = None

for line in sys.stdin:
    bi, count = line.strip().split('\t', 1)
    try:
        count = int(count)
    except ValueError:
       continue
    if current_bi == bi:
        current_count += count
    else:
        if current_bi:
            print '%s\t%s' % (current_bi, current_count)
        current_count = count
        current_bi = bi

if current_bi == bi:
    print '%s\t%s' % (current_bi, current_count)  
#%%
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    