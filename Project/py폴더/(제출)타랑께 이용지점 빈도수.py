#!/usr/bin/env python
# coding: utf-8

# In[1]:


#타랑께 이용지점 빈도수
import pandas as pd


# In[2]:


타랑께 = pd.read_csv('타랑께_최종.csv',index_col = 0)#타랑께 정보 데이터 불러오기


# In[7]:


타랑께_사용량 = pd.read_csv('자전거_사용시간.csv',index_col = 0,encoding = 'cp949')


# In[9]:


타랑께


# In[10]:


타랑께.columns


# In[17]:


#타랑께 출발지점 추출
타랑께_지점 = 타랑께.loc[:,['출발지']]


# In[18]:


타랑께_지점


# In[16]:


import numpy as np


# In[24]:


count=타랑께_지점['출발지'].value_counts() #각 출발지점 빈도 수 추출


# In[25]:


count


# In[26]:


빈도수 = pd.DataFrame(count) #데이터프레임화


# In[27]:


빈도수


# In[31]:


빈도수.to_csv('freq_station.csv',index = True,encoding='cp949')


# In[ ]:




