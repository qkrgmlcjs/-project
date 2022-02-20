#!/usr/bin/env python
# coding: utf-8

# In[3]:


#서울2030인구,사용량 상관관계
# Data
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

#warning
import warnings
warnings.filterwarnings('ignore')


# In[3]:


pip install plotly


# In[4]:


자치구나이 = pd.read_csv('자치구나이.csv',encoding = 'utf-8') #서울 자치구별 20,30대 인구,사용량
자치구나이


# In[5]:


서울인구 = pd.read_csv('서울 인구.csv',encoding = 'utf-8')#서울 자치구별 전체 인구


# In[6]:


서울인구test=서울인구[['자치구','계']]


# In[7]:


서울인구test


# In[8]:


plt.rcParams['font.family'] = 'Malgun Gothic' #한글 출력 위해 글꼴 설정하기


# In[9]:


corr = 자치구나이.corr(method = 'pearson') #2030인구수 와 자전거 사용량의 상관관계 구하가 피어슨계수


# In[10]:


df_heatmap = sns.heatmap(corr, cbar = True, annot = True, annot_kws={'size' : 20}, fmt = '.2f', square = True, cmap = 'Blues')
plt.rcParams['font.family'] = 'Malgun Gothic' #한글 출력 위해 글꼴 설정하기
#상관관계 히트맵 그리기


# In[ ]:




