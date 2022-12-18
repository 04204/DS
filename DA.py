from datascience import *
import plotly.express as px
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('Agg')
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
url = 'https://raw.githubusercontent.com/04204/DS/main/%E4%BE%86%E5%8F%B0%E7%9B%AE%E7%9A%84.csv'
df1 = pd.read_csv(url, header=0)
month = 1
year = 108
目的 = ['業務','觀光','探親','會議','求學','展覽','醫療','其他']
while(year <= 111):
    while(month <= 12):
        if(year==111 and month >10):
            break
        if month >= 10:
            time = str(year)+'/'+str(month)
        else:
            time = str(year)+'/0'+str(month)
        month += 1
        plt = px.bar(df1[df1['時間']==time], x='居住地', y=目的, barmode='group',title=f'各大洲來台目的 {time}').update_layout(yaxis_title="人數",legend_title_text="目的")
        plt.show()
        
    month = 1
    year += 1