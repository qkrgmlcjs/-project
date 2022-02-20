#!/usr/bin/env python
# coding: utf-8

# In[26]:


#타랑께 이용지점 빈도수
import pandas as pd
import numpy as np
a = pd.read_csv('자전거_사용시간_최종.csv',index_col = 0,encoding = 'cp949')
df = pd.DataFrame(a)

df


# # 월별 현황

# In[3]:


start=[] 
for x in range(0, len(df)):
    start.append(df['출발시각'][x]) #출발시각 열 추출
type(start)


# In[4]:


start[0]


# In[5]:


start[0][0:4] #연도추출


# In[6]:


start[0][5:7] 


# In[7]:


month = []
for i in range(0, len(df)):
    month.append(start[i][5:7]) #월 추출


# In[8]:


len(month)


# In[9]:


print(month.count('07'))


# In[10]:


dict = {}  #월별 이용량 추출 키,밸류 방식
for v in month:
    if dict.get(v): dict[v]+=1
    else : dict[v]=1
        
print(dict)


# In[11]:


y = (list(dict.values()))# 월별 이용량 밸류 값 리스트 지정
x = (list(dict.keys()))#월별 키값 리스트


# In[12]:


print(x)
print(y)


# --------

# # 시간대별 현황

# In[13]:


usage=[]
for x in range(0, len(df)):
    usage.append(df['사용시간'][x]) #사용시간 열 추출
type(usage)


# In[14]:


usage[0] 


# In[15]:


usage[0][10:12]


# In[16]:


minute = []
for i in range(0, len(df)):
    minute.append(usage[i][10:12]) #사용시간 (분 추출)


# In[17]:


minute.sort()


# In[18]:


dict1 = {}
for v in minute:
    if dict1.get(v): dict1[v]+=1   
    else : dict1[v]=1   #시간대 별 이용량 추출
        
print(dict1)


# In[19]:


x = (list(dict1.keys()))
y = (list(dict1.values()))


# In[20]:


print(x)
print(y)


# In[21]:


y[0:10]


# In[22]:


minute_by_10 = []   #시간대별 시각화 위해 10분 단위로 이용량 나누기
division = [10, 20, 30, 40, 50, 60]
for i in division:
    a = sum(y[i-10:i])
    minute_by_10.append(a)


# In[23]:


minute_by_10


# In[24]:


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.xlabel('탑승시간')
plt.ylabel('이용건수')
plt.bar(division, minute_by_10, width=6) #시간대별 시각화
plt.show()


# In[ ]:





# In[25]:


import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

plt.bar(x, y)
plt.xlabel('월')
plt.ylabel('이용건수')
plt.show()


# In[ ]:





# In[ ]:




