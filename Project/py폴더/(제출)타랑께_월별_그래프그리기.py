#!/usr/bin/env python
# coding: utf-8

# In[1]:


#타랑께 월별 그래프 그리기
import numpy as np

import pandas as pd

from matplotlib import pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic' #한글 출력 위해 글꼴 설정하기


# In[3]:


august = pd.read_csv('2020_8.csv',index_col = 0,encoding = 'cp949')


# In[4]:


august


# In[5]:


august.columns


# In[6]:


df_list = august['시간']
df_list2 = august['사용량']


# In[7]:


df_list=df_list.tolist()
df_list2 = df_list2.tolist()


# In[8]:


label = august.index
label


# In[9]:


index = np.arange(len(label)-1)


# In[ ]:





# In[10]:


y = df_list2
x = df_list

plt.bar(x,y,width = 0.7,color = "blue")
plt.xlabel('시간')
plt.ylabel('사용량')
plt.title('8월 시간대별 사용량')

plt.show()


# In[11]:


august.describe()


# In[12]:


use_time_7 = pd.read_csv('2020_7.csv',index_col = 0,encoding = 'cp949')
use_time_8 = pd.read_csv('2020_8.csv',index_col = 0,encoding = 'cp949')
use_time_9 = pd.read_csv('2020_9.csv',index_col = 0,encoding = 'cp949')
use_time_10 = pd.read_csv('2020_10.csv',index_col = 0,encoding = 'cp949')
use_time_11= pd.read_csv('2020_11.csv',index_col = 0,encoding = 'cp949')
use_time_12= pd.read_csv('2020_12.csv',index_col = 0,encoding = 'cp949')
use_time_21_1 = pd.read_csv('2021_1.csv',index_col = 0,encoding = 'cp949')
use_time_21_2 = pd.read_csv('2021_2.csv',index_col = 0,encoding = 'cp949')


# In[13]:


graph_month = [use_time_7,use_time_8,use_time_9,use_time_10,use_time_11,use_time_12,use_time_21_1,use_time_21_2]


# In[14]:


cols = ['시간','사용량']


# In[15]:



for i in range(len(graph_month)):
    
    use_time = graph_month[i]

    use_time_y = use_time['사용량']
    use_time_x = use_time['시간']
    plt.bar(use_time_x,use_time_y,width = 0.5,color = "green")

    #plt.subplot(3, 3, (i%3)+1)
    plt.xlabel('시간')
    plt.ylabel('사용량')
    if((i+7)%13 == 0) :
        plt.title(f'{(i+7)%13+1} 월 시간대별 사용량')
    elif ((i+7)%13 == 1) :
        plt.title(f'{(i+7)%13+1} 월 시간대별 사용량')
    else :
        plt.title(f'{(i+7)%13} 월 시간대별 사용량')
    
    plt.grid()
    plt.show()


# In[ ]:




