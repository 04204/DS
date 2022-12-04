from datascience import *
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('Agg')
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
fig = plt.figure(figsize = (20,12))
ax1 = fig.add_subplot(1,1,1)
url = 'https://raw.githubusercontent.com/04204/DS/main/%E6%AD%B7%E5%B9%B4%E4%BE%86%E5%8F%B0%E6%97%85%E5%AE%A2%E5%9C%8B%E7%B1%8D%E7%B5%B1%E8%A8%882002-2021.csv'
df = pd.read_csv(url, header=0)

total = '總計 Grand Total'
all = df[df['細分']==total]
asia = df[df['細分']=='亞洲合計 Total']
afr = df[df['細分']=='非洲合計 Total']
ame = df[df['細分']=='美洲合計 Total']
ocea = df[df['細分']=='大洋洲合計 Total']
eu = df[df['細分']=='歐洲合計 Total']
year = 2002
years = []
year_total = []
asia_total = []
afr_total = []
ame_total = []
ocea_total = []
eu_total = []

while(year<=2021):
    years.append(year)
    year_total.append(int(all[str(year)].values[0].replace(",", "")))
    asia_total.append(int(asia[str(year)].values[0].replace(",", "")))
    afr_total.append(int(afr[str(year)].values[0].replace(",", "")))
    ame_total.append(int(ame[str(year)].values[0].replace(",", "")))
    ocea_total.append(int(ocea[str(year)].values[0].replace(",", "")))
    eu_total.append(int(eu[str(year)].values[0].replace(",", "")))
    year += 1

x = np.arange(0, len(years), 1)
ax1.plot(x, year_total,color='#C42022',marker='o',markersize=4)
ax1.set_xticks(x)
ax1.set_xticklabels(years)
#plt.xticks(rotation=90)

for x,y in zip(x, year_total):
    plt.text(x,y+10,'%.0f' %y,ha='center',color='#6D6D6D',fontsize=10)
plt.title('2002-2021',color='#6D6D6D',fontsize=15)
plt.xlabel('Year')
plt.ylabel('Total(10M)')
plt.show()

fig = plt.figure()
labels = ["ASIA","OCEA","EU","AME","AFR"]
i=0
ASIA=0
OCEA=0
EU=0
AME=0
AFR=0

while(i<len(years)):
  ASIA+=asia_total[i]
  OCEA+=ocea_total[i]
  EU+=eu_total[i]
  AME+=ame_total[i]
  AFR+=afr_total[i]
  i+=1

plt.title('2002-2022',color='#6D6D6D',fontsize=15)
word_size = [ASIA,OCEA,EU,AME,AFR]
explode = [.05, 0, 0, 0, 0]  
plt.pie(word_size, explode= explode, labels = labels, autopct= "%3.1f%%")
plt.show()

fig = plt.figure(figsize = (25,10))
ax1 = fig.add_subplot(1,1,1)
url = 'https://raw.githubusercontent.com/04204/DS/main/data.csv'
df = pd.read_csv(url, header=0)

asia_total = df[df['居住地']=='亞洲合計 Total']
asia_all = []
ocea_total = df[df['居住地']=='大洋洲合計 Total']
ocea_all = []
eu_total = df[df['居住地']=='歐洲合計 Total']
eu_all = []
ame_total = df[df['居住地']=='美洲合計 Total']
ame_all = []
afr_total = df[df['居住地']=='非洲合計 Total']
afr_all = []
all = []

ptime = []
year = 108
month = 9
while(year <= 111):
    while(month <= 12):
        if(year==111 and month >=10):
            break
        time = str(year)+'年'+str(month)+'月'
        asia_all.append(int(asia_total[time].values[0]))
        ocea_all.append(int(ocea_total[time].values[0]))
        eu_all.append(int(eu_total[time].values[0]))
        ame_all.append(int(ame_total[time].values[0]))
        afr_all.append(int(afr_total[time].values[0]))
        all.append((int(asia_total[time].values[0])+int(ocea_total[time].values[0])+int(eu_total[time].values[0])+int(ame_total[time].values[0])+int(afr_total[time].values[0])))
        ptime.append(time.replace("年", "/").replace("月",""))
        month += 1
    month = 1
    year += 1

ax1.plot(ptime,all,color='#1f77b4',marker='o',markersize=4,label='Total')
ax1.plot(ptime,asia_all,color='#ff7f0e',marker='o',markersize=4,label='Asia')
ax1.plot(ptime,ocea_all,color='#2ca02c',marker='o',markersize=4,label='Oceania')
ax1.plot(ptime,eu_all,color='#d62728',marker='o',markersize=4,label='Europe')
ax1.plot(ptime,ame_all,color='#9467bd',marker='o',markersize=4,label='Americas')
ax1.plot(ptime,afr_all,color='#8c564b',marker='o',markersize=4,label='Africa')


plt.title('2019-2022',color='#6D6D6D',fontsize=20)
plt.xlabel('Time')
plt.ylabel('Total(1M)')
plt.legend(loc = 'lower left')
plt.show()

fig = plt.figure()
labels = ["ASIA","OCEA","EU","AME","AFR"]
i=0
ASIA=0
OCEA=0
EU=0
AME=0
AFR=0

while(i<len(ptime)):
  ASIA+=asia_all[i]
  OCEA+=ocea_all[i]
  EU+=eu_all[i]
  AME+=ame_all[i]
  AFR+=afr_all[i]
  i+=1

plt.title('2019-2022',color='#6D6D6D',fontsize=15)
word_size = [ASIA,OCEA,EU,AME,AFR]
explode = [.05, 0, 0, 0, 0]  
plt.pie(word_size, explode= explode, labels = labels, autopct= "%3.1f%%")
plt.show()