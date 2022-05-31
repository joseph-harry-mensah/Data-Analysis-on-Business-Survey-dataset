#!/usr/bin/env python
# coding: utf-8

# In[177]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[209]:


df=pd.read_excel('Business Survey (Responses).xlsx')


# In[210]:


df


# In[211]:


df.shape


# In[212]:


df.replace('Watsapp','Whatsapp')


# In[ ]:





# ### Entrepreneurs Responses

# In[213]:


#Are you an entrepreneur

Entrepreneur = df[df['Are you a student entrepreneur?']=="Yes"]
Entrepreneur.shape


# In[255]:


Entrepreneur.head(3)


# In[326]:


#Business w/n student as Clients vrs Business without student clients


business_clients= df['Clients']
business_clients.value_counts().plot(kind='bar', ylabel='Client type Counts', color='green',
                             figsize=(5,5), title='Business w/n students as Clients vrs Business without student clients')


# In[325]:


#What type of business do you do? ---Overall Businesses

business_type=df['Business Industry']
business_type.value_counts().plot(kind='barh', ylabel='Business Counts', xlabel='Business industry',
                                 color='green', figsize=(8,8))


# ## Analysis on Business have  student clients
# 

# In[254]:


#Types of business who have students as clients

stu_clients_business= df[df['Clients']=='Student Clients']
stu_clients_business.head(2)


# In[249]:


#What business serve only students as their clients

serve_onlystudents = stu_clients_business[stu_clients_business['Does your business serve students only?']=='Yes']
serve_onlystudents['Business Industry'].hist(figsize=(15,6), color='blue')


# **Business that serve only students**

# In[250]:


#What business serve  students and other clients

serve_everyone = stu_clients_business[stu_clients_business['Does your business serve students only?']=='No']
everyone = serve_everyone['Business Industry'].value_counts()

everyone.plot(kind='barh', figsize=(5,5), color='blue')


# ### Business that don't have Clients as Students

# In[317]:


no_stu = df[df['Clients']=='None Student Clients']
no_studentclients = no_stu['What type of business do you do?']
no_studentclients.value_counts().plot(kind='barh',color='darkblue')


# 

# 

# # Why did you choose this type of business?

# In[296]:


#Why did you choose this type of business?

choice = df['Influence on Industry Choice']
reasons = choice.value_counts().plot(kind='barh', color='darkgreen', title='Reasons for Venturing Business')
reasons


# In[302]:


#What platform(s) do you advertise your business on?

platforms= df['What platform(s) do you advertise your business on?']
platform = platforms.value_counts().plot(kind='barh', color='darkgreen', figsize=(8,8))


# In[344]:


#What challenges did you face when you started your business?


chall = df['Challenges']
challenges = chall.value_counts().plot(kind='barh', color='darkblue', figsize=(8,8), title='Challenges Entrepreneurs faced in starting their businesses')


# In[323]:


#Mode of Payment


money = df['Mode of Payment']
mode_of_payment = money.value_counts().plot(kind='barh',  figsize=(6,6), title="Mode of Payments")


# In[329]:


#How do you get your products to your customers?

deliv = df['Delivery']
delivery = deliv.value_counts().plot(kind='barh',  figsize=(6,6), title="Mode of Payments")


# In[ ]:





# In[333]:


#Can you tell us your most used delivery service if any?


most_deliv = df['Most used Delivery Service']
most_delivery = most_deliv.value_counts().plot(kind='barh', color='blue', figsize=(6,6), title="Most Used delivery service")


# In[343]:


#If you would like to be a part of a product test that aims to help student and small scale businesses, kindly give us your phone number (Whatsapp)


resp = df['Interested']
response = resp.value_counts().plot(kind='bar', color='blue',  figsize=(4,5), title="No of Entrepreneurs Interested In Product Testing in")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


Twitter = (stu_clients['What platform do most of your customers reach you through?'].value_counts()['Twitter'])

Snapchat = (stu_clients['What platform do most of your customers reach you through?'].value_counts()['Snapchat'])
LinkedIn = (stu_clients['What platform do most of your customers reach you through?'].value_counts()['LinkedIn'])


# In[ ]:





# In[ ]:





# In[ ]:




