#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:05:49 2017

@author: zhechengma
"""
import pandas as pd 
import pymysql

conn=pymysql.connect(host='192.168.20.180',port=3306,user='miqixin_mo',password='miqixin_mo8812345',db='miqixin',charset='utf8')
conn=pymysql.connect(host='590a883d68e3f.sh.cdb.myqcloud.com',port=8904,user='root',password='mazc1990',db='linshiwanwan',charset='utf8')

df1=pd.read_sql('select * from names_lists limit 0,1000000',con=conn)


del df1['uid'],df1['old_name'],df1['province'],df1['city'],df1['county'],df1['pid'],df1['is_show'],df1['addtime'],df1['chongfu'],df1['is_cecdc'],df1['is_exposure'],df1['cecdc_type'],df1['cecdc_sort'],df1['cecdc_date'],df1['class']
I=[]
for i in range(len(df1)):
    j=df1.ix[i].isnull().sum()/len(df1.ix[i])
    I.append(j)
    
df1['null_count']=I

df1['null_count'].describe()

df2=pd.read_sql('select name from needs_check',conn)

import re
string = 'dsfbnjkg.innoi'
regex = re.compile('txt$')
result = regex.match(string)
print(result)

d_n = list(df2['name'])

_m=d_n.copy()

for i in d_n:
    gg=regex.match(i)
    if gg:
        _m.remove(gg.group(0))

d_n=_m
    
import matplotlib.pyplot as plt

plt.hist(I,50,normed=1,facecolor='r',alpha=1)
plt.xlabel('分布')
plt.ylabel('频率')
plt.title('错误分布律')
plt.grid(True)

haslen(df1[df1['null_count']>0.18].creation_date)/len(df1)