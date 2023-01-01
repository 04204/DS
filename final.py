from datascience import *
import plotly.express as px
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib
import pandas as pd
matplotlib.use('Agg')
#%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')
url = 'https://raw.githubusercontent.com/04204/DS/main/%E4%BE%86%E5%8F%B0%E7%9B%AE%E7%9A%84.csv'
df1 = pd.read_csv(url, header=0)
df_total = pd.DataFrame(columns = ['居住地','合計','業務','觀光','探親','會議','求學','展覽','醫療','其他','時間'])
df_co = pd.DataFrame(columns = ['居住地','合計','業務','觀光','探親','會議','求學','展覽','醫療','其他','時間'])
df_coV = pd.DataFrame(columns = ['居住地','合計','業務','觀光','探親','會議','求學','展覽','醫療','其他','時間'])
df_pre = pd.DataFrame(columns = ['居住地','合計','業務','觀光','探親','會議','求學','展覽','醫療','其他','時間'])

month = 1
year = 108
目的 = ['業務','觀光','探親','會議','求學','展覽','醫療','其他']
目的V = ['業務','觀光','探親','會議','求學','展覽','醫療']
count = 0
while(year <= 111):
    while(month <= 12):
        if(year==111 and month >10):
            break
        if month >= 10:
            time = str(year)+'/'+str(month)
        else:
            time = str(year)+'/0'+str(month)
        month += 1
        df2 = df1[df1['時間']==time]
        count += 1
        if count <=12:
            df_pre.loc[len(df_total)] = ['總計',df2['合計'].sum(),df2['業務'].sum(),df2['觀光'].sum(),df2['探親'].sum(),df2['會議'].sum(),df2['求學'].sum(),df2['展覽'].sum(),df2['醫療'].sum(),df2['其他'].sum(),time]
        if count > 12:
            df_coV.loc[len(df_total)] = ['總計',df2['合計'].sum(),df2['業務'].sum(),df2['觀光'].sum(),df2['探親'].sum(),df2['會議'].sum(),df2['求學'].sum(),df2['展覽'].sum(),df2['醫療'].sum(),df2['其他'].sum(),time]
        if count >= 15:
            # 109/03後的數據 折線圖用
            df_co.loc[len(df_total)] = ['總計',df2['合計'].sum(),df2['業務'].sum(),df2['觀光'].sum(),df2['探親'].sum(),df2['會議'].sum(),df2['求學'].sum(),df2['展覽'].sum(),df2['醫療'].sum(),df2['其他'].sum(),time]
        # 全體數據 折線圖用
        df_total.loc[len(df_total)] = ['總計',df2['合計'].sum(),df2['業務'].sum(),df2['觀光'].sum(),df2['探親'].sum(),df2['會議'].sum(),df2['求學'].sum(),df2['展覽'].sum(),df2['醫療'].sum(),df2['其他'].sum(),time]
        plt = px.bar(df2, x='居住地', y=目的, barmode='group',title=f'各大洲來台目的 {time}').update_layout(yaxis_title="人數",legend_title_text="目的")
        # 下載圖表
        # plt.write_image("./"+"各大洲來台目的_"+str(year)+"_"+str(month)+".png")
        #plt.show()
        
    month = 1
    year += 1

df_total.to_csv('total.csv',index=False,encoding='utf8')
df_co.to_csv('co.csv',index=False,encoding='utf8')
df_coV.to_csv('coV.csv',index=False,encoding='utf8')
df_pre.to_csv('pre.csv',index=False,encoding='utf8')
print('done')
