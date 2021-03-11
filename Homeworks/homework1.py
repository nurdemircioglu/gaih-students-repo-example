#!/usr/bin/env python
# coding: utf-8

# In[1]:


dizi1=[1,3,5,7,9,11,13,15,17,19,21]
print(dizi1)


# In[2]:


dizi2=[2,4,6,8,10,12,14,16,18]
print(dizi2)


# In[3]:


dizi1.extend(dizi2)
print(dizi1)


# In[5]:


yeniList = [x*2 for x in dizi1]
print(yeniList)


# In[16]:


len(yeniList)


# In[17]:


yeniListType = [type(yeniList[x]) for x in range(0,20)]
print(yeniListType)

