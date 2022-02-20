#!/usr/bin/env python
# coding: utf-8

# In[2]:


#타랑께 사용량
import pandas as pd
#타랑께 사용량 데이터 불러오기
자전거 = pd.read_csv('(제출)타랑께_최종.csv',index_col = 0)
#출발시각,도착시각 추출
내자전거 = 자전거.loc[:, ['출발시각', '도착시각']]


# In[5]:


자전거_출발 = 내자전거['출발시각']
자전거_출발


# In[6]:


자전거_도착 = 내자전거['도착시각']
자전거_도착


# In[7]:


자전거_출발 =자전거_출발.astype('str')
자전거_도착 =자전거_도착.astype('str')


# In[9]:


from datetime import date,datetime,time
df_list=[]
for i in 자전거_출발 : # 출발시각 Str형식 Date형식 으로 변환
    date = i
    c_date = datetime.strptime(date,"%Y%m%d%H%M%S")
    c_date=c_date.strftime('%Y-%m-%d %H:%M:%S')
    df_list.append(c_date)


# In[10]:


df_list_3=[]
for a in 자전거_도착 :#도착시각 Str형식 Date형식 으로 변환
    date_a = a
    c_date = datetime.strptime(date_a,"%Y%m%d%H%M%S")
    c_date=c_date.strftime('%Y-%m-%d %H:%M:%S')
    df_list_3.append(c_date)


# In[11]:


df_출발 = pd.DataFrame(df_list)
df_도착 = pd.DataFrame(df_list_3)
자전거_시간 = pd.concat([df_출발,df_도착],axis=1)
자전거_시간.columns = ['출발시각','도착시각']


# In[12]:


자전거_시간['출발시각'] = pd.to_datetime(자전거_시간['출발시각'])
자전거_시간['도착시각'] = pd.to_datetime(자전거_시간['도착시각']) #데이트타임형식으로 변경


# In[13]:


자전거_시간


# In[10]:


자전거_시간= 자전거_시간.transpose()
자전거_시간.loc['사용시간'] = 자전거_시간.loc['도착시각']- 자전거_시간.loc['출발시각'] #사용시간 계산 및 칼럼 생성


# In[11]:


자전거_시간 = 자전거_시간.T


# In[12]:


자전거_시간


# In[ ]:




