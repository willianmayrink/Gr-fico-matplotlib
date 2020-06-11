import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np

df= pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')
df= df.sort_values(by=['Date'])
df['Date']= pd.to_datetime(df['Date'])
df= df.set_index('Date')
a2015= df.loc['20150101':'20151231']
df= df.loc['20050101':'20141231']
df= df.reset_index()
df['Month']= df['Date'].dt.month
df['Day']= df['Date'].dt.day
df= df.sort_values(by=['Month','Day'])
x= df.groupby(['Month', 'Day'])['Data_Value'].agg({'max': np.max, 'min': np.min})
x=x.reset_index()

x= x.drop(x.index[59])
x=x.reset_index()

a2015=a2015.reset_index()
a2015['Month']= a2015['Date'].dt.month
a2015['Day']=a2015['Date'].dt.day
a2015= a2015.sort_values(by=['Month','Day'])
y= a2015.groupby(['Month', 'Day'])['Data_Value'].agg({'max': np.max, 'min': np.min})
y= y.reset_index()
m= np.arange(1,366,1)
f= pd.date_range('1/1/2017', periods=365) #Testar isso aqui dps com os dias como data


df1=pd.Series()
df1['Max'] = np.where(y['max'] > x['max'], y['max'] , None)
df1['Min'] = np.where(y['min'] < x['min'], y['min'] , None)

plt.figure()
plt.plot(m, df1['Max'], 'o', m , df1['Min'], 'o', m , x['max'] , '-o' , m,x['min'] ,'-o')
plt.gca().fill_between(range(len(x['min'])), 
                       x['min'],x['max'] , 
                       facecolor='blue', alpha=0.25)
plt.ylabel('Temperatura (F)') 
plt.xlabel('Tempo (dias)') 

plt.show()
