# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 16:06:22 2019

@author: sivak
"""
import pandas as pd
import numpy as np
def convertfn (dataframe1,b,x):
    df3 = dataframe1.loc[:,b]
    df3['Total'] = pd.Series(np.random.randn(), index=df3.index)
    df3['Attended'] = pd.Series(np.random.randn(), index=df3.index)
    df3['percentile'] = pd.Series(np.random.randn(), index=df3.index)
    df3['gradePoints'] = pd.Series(np.random.randn(), index=df3.index)
    df3['targetAchieved'] = pd.Series(np.random.randn(), index=df3.index)
    a=0.0
    for index,row in df3.iterrows():
        a=0.0
        for l in b:
            print(np.isnan(row[l]))
            if(row[l]!=row[l]):
                print('hello') 
            else :
                a = a+row[l];
        row['Total']=a;
    a=0.0
    for index,row in df3.iterrows():
        a=0.0
        for l in b:
            if(np.isnan(row[l])):
                print('hello') 
            else :
                a = a+dataframe1.loc[0,l];
        row['Attended']=a;
    for index,row in df3.iterrows():
        row['percentile']=row['Total']/row['Attended']*100
        if(row['percentile'] > 60):
            row['gradePoints']=3
            row['targetAchieved']='1'
        elif (row['percentile'] > 40):
            row['gradePoints']=2
            row['targetAchieved']='0'
        else :
            row['gradePoints']=1
            row['targetAchieved']='0'
    c=[]
    c.insert(0,'Register No.')
    c.insert(1,'Student Name')
    df5=df.loc[:,c]
    df5.head()
    frames = [df5,df3]
    df4 = pd.concat(frames,axis=1, sort = False)
    df4.to_csv(x,index = False)
    
    
x = input("enter the ip csv file : ")
y = input("enter the co map csv file : ")
z = input("enter the op csv file name alone : ")
df = pd.read_csv(x)
df2 = pd.read_csv(y)
for i in range(0,5):
    b1= df2.T1[i]
    if isinstance(b1,str):
        b=b1.split(',')
    a= df2.T2[i]
    if isinstance(a,str):
        a=a.split(',')
        if isinstance(b1,(str)):
            for j in a:
                b.append(j)
        else:
            b=a
    print(b)        
    convertfn(df,b,z+str(i)+'.csv')
