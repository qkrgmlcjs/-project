#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[2]:


from html import unescape


# In[7]:


with open('dp.html') as f:
    html = f.read()


# In[8]:


#re.findall()을 사용해  도서 하나에 해당하는 HTML을 추출합니다.


# In[10]:


for partial_html in re.findall(r'<td class="left"<a.*?</td>',html,re.DOTALL):
    url = re.search(r'<a href="(.*?)">',partial_html).group(1)
    url = 'http://www.hanbit.co.kr' + url
    title = re.sub(r'<.*?>','',partial_html)
    title = unescape(title)
    print('url:',url)
    print('title:' ,title)
    print('---')


# In[ ]:




