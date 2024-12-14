#!/usr/bin/env python
# coding: utf-8

# In[32]:

!pip install numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns





# In[27]:


# Load the dataset
df = pd.read_csv(r"C:\Users\yashv\Desktop\InstagramThreads_Reviews-Data-1.csv")


# In[5]:


#exploring the dataset
df.head()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


#Data preprocessing and cleaning
df.isnull().sum()


# In[9]:


#dropping NA values if any
df.dropna(inplace=True)


# In[10]:


df.describe()


# In[11]:


df.info()


# In[12]:


#Convert 'review_date' to datetime

df['review_date'] = pd.to_datetime(df['review_date'])


# In[13]:


df.head()


# In[14]:


#exploritory data analysis

#Mean rating by platform
mean_rating_by_platform = df.groupby('source')['rating'].mean()
print(mean_rating_by_platform)


print('\n')

#median rating by platform
median_rating_by_platform = df.groupby('source')['rating'].median()
print(median_rating_by_platform)

print('\n')

#mode rating by platform
mode_rating_by_platform = df.groupby('source')['rating'].agg(pd.Series.mode)
print(mode_rating_by_platform)


# In[15]:


#visual represntation

import matplotlib.pyplot as plt
#bar graph for mean ratings


mean_rating_by_platform.plot(kind='bar')
plt.title('Mean Rating by Platform')
plt.xlabel('Platform')
plt.ylabel('Mean Rating')
plt.show()

#Mean rating is better on google play store


# In[16]:


#boxplot for median rating by platform
sns.boxplot(x='source', y='rating', data=df)
plt.title('Median Rating by Platform')
plt.xlabel('Platform')
plt.ylabel('Median Rating')
plt.show()


#median is better on the google playstore


# In[17]:


#pie chart for number of ratings per platform
mode_rating_by_platform.plot(kind='pie')
plt.title('Mode Rating by Platform')
plt.show()

#Google play has substantially better mode rating


# In[18]:


#Number of reviews by platform
reviews_by_platform = df['source'].value_counts()
print(reviews_by_platform)




# In[19]:


#Mean rating over time

mean_rating_over_time = df.groupby('review_date')['rating'].mean()
print(mean_rating_over_time)
'''plt.plot(mean_rating_over_time)
plt.title('Mean Rating Over Time')
plt.xlabel('Date')
plt.ylabel('Mean Rating')
plt.show()'''


# In[20]:


#Number of reviews over time
reviews_over_time = df['review_date'].value_counts()
print(reviews_over_time.head())
print(reviews_over_time.tail())

print('\n')

#visualization

plt.hist(df['review_date'],bins = 20)

plt.xlabel('Review Date')
plt.ylabel('Number of Reviews')
plt.title('Number of Reviews by Date')


# Rotate x-axis labels for better readability
plt.xticks(rotation=45)
plt.show()


# In[21]:


# Distribution of ratings
plt.figure(figsize=(10, 5))
sns.histplot(df['rating'], bins=10, kde=True)
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Frequency')
plt.show()




# In[ ]:





# In[26]:


#generating word cloud
#!pip install wordcloud
from wordcloud import WordCloud
# Randomly select 30-50 reviews
sample_reviews = df['review_description'].sample(50).values

# Generate
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(sample_reviews))

# Display
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




