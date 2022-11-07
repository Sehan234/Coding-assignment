#!/usr/bin/env python
# coding: utf-8

# In[39]:


# Task 2
import random


# In[40]:


x = random.sample(range(0,1001),50) # Generate 50 random numbers between 0 and 1000


# In[41]:


rl = open('random50.txt','w') # Create a new text file with the name random50.txt in write mode


# In[42]:


for item in x:
    rl.write("%s\n" % item)  # Write each element in the random list x into the text file


# In[43]:


rl.close() # Close the text file


# In[44]:


# Task 3
even = [] # Make empty list to append even random numbers
for item in x:
    if item % 2 == 0: # Check whether random number divisible by 2
        even.append(item) # Append values to list


# In[49]:


even.sort() # Sort numbers from smallest to largest


# In[50]:


rle = open('randomeven.txt','w') # Create new text file with the name randomeven.txt in write mode


# In[51]:


for item in even:
    rle.write("%s\n" % item)  # Write each element in the even list to the text file


# In[52]:


rle.close() # Close the file

