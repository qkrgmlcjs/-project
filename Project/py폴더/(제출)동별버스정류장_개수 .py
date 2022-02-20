#!/usr/bin/env python
# coding: utf-8

# In[3]:


#동별버스정류장 개수
import pandas as pd

주소 = pd.read_csv('버정위치.csv',index_col = 0,encoding='cp949')#버스정류장 위치 로드


# In[4]:


주소


# In[5]:


주소_동 = 주소.loc[:,['설치장소']] #설치 동 추출


# In[20]:


주소_동


# In[21]:


count = 주소_동.value_counts() #동별 정류장 개수 집계


# In[22]:


count 


# In[23]:


동별_개수 = pd.DataFrame(count)


# In[25]:


동별_개수.index


# In[26]:


동별_개수.to_csv('동별버정개수.csv',index = True,encoding='cp949')#csv파일로 추출


# In[51]:


동별_개수= pd.read_csv('동별버정개수.csv',index_col=0,encoding = 'cp949')


# In[52]:


동별_개수


# In[70]:


#광주 전체인구 csv파일 불러오기
광주종합 = pd.read_csv('광주전체.csv',index_col=0,encoding = 'cp949')


# In[71]:


광주종합


# In[72]:


# 광주동별인구, 동별 버스정류장 개수 조인
df_inner_join = pd.merge(광주종합,동별_개수,
                        left_on='key',right_on='key',how='inner') 


# In[73]:


df_inner_join


# In[74]:


df_inner_join.to_csv('pop_station_final.csv',index=True,encoding='cp949')


# In[ ]:




