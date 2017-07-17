#encoding = utf8

import pandas as pd

df1=pd.read_csv('c_base.txt',sep=',')
df2=pd.read_csv('c_branch.txt',sep=',')


#names_list=list(df1['name'])

a=[]
b=[]
for i in range(len(df1['name'])):
	if df1['name'][i] in df2['brName']:
		print(df1['name'][i])
		a.append(df1['id'][i])
		b.append(df2['brName'][i])


_name = pd.Series(b)
idl=pd.Series(a)
df3=pd.DataFrame(idl,_name)
print(df3)

# df3.to_csv('namess.csv',encoding='utf8')


		
