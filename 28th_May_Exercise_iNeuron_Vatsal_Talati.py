#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = 4
for i in range(4) :
    for j in range(i+1) :
        print("ineuron", end = " ")
    print("\n")


# In[2]:


s = "ineuron"
n = 3
p = n-2
m = n-1
d = p-1
for i in range(n) :
    for j in range(i+1) :
        if m>0 :
            for k in range(m) :
                print(" " * len(s), end = "")
        print(s, " " * len(s), end="")
        m = m-1
    print("\n")

for q in range(p,0,-1) :
    for r in range(q+1) :
        if d<=2 :
            for g in range(d) :
                print(" " * len(s), end="")
        print(s, " " * len(s), end="")
        d = d+1
    print("\n")


# In[3]:


l = [[1,2,3,4], (2,3,4,5,6), (3,4,5,6,7), set([23,4,5,45,4,4,5,45,45,4,5]), {"k1":"sudh", "k2":"ineuron", "k3":"kumar", 3:6, 7:8}, ["ineuron", "data science"]]


# In[4]:


for i in l :
    if type(i) == list :
        print(i)


# In[5]:


for i in l :
    if type(i) == dict :
        print(i)


# In[6]:


for i in l :
    if type(i) == tuple :
        print(i)


# In[7]:


for i in l :
    for j in i :
        if type(j) == int :
            if type(i) == dict :
                if type(i[j]) == int :
                    print(i[j])
            print(j)


# In[8]:


sum = 0
for i in l :
    for j in i :
        if type(j) == int :
            if type(i) == dict :
                if type(i[j]) == int :
                    sum = sum + i[j]
            sum = sum + j
print(sum)


# In[9]:


for i in l :
    if type(i) == list :
        for j in i :
            if j % 2 != 0 :
                print(j)


# In[10]:


for i in l :
    if type(i) == list or type(i) == dict or type(i) == set or type(i) == tuple :
        for j in i :
            if j == "ineuron" :
                print(j)
    if type(i) == dict :
        for j in i :
            if i[j] == "ineuron" :
                print(i[j])
    if i == "ineuron" :
        print(i)


# In[11]:


l2 = []
for i in l :
    if type(i) == list or type(i) == dict or type(i) == set or type(i) == tuple :
        for j in i :
            l2.append(j)
    if type(i) == dict :
        for j in i :
            l2.append(i[j])

for k in set(l2) :
    print(k, ":", l2.count(k))


# In[12]:


key_val = 0
key_count = 0
for i in l :
    if type(i) == dict :
        key_val = i.keys()
        for j in key_val :
            key_count = key_count + 1
        print(key_count)


# In[13]:


for i in l :
    if type(i) == dict or type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == str :
                print(j)
    if type(i) == dict :
        for j in i :
            if type(i[j]) == str :
                print(i[j])
    if type(i) == str :
        print(i)


# In[14]:


l3 = []
for i in l :
    if type(i) == dict or type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == str :
                if j.isalnum() :
                    l3.append(j)
    if type(i) == dict :
        for j in i :
            if type(i[j]) == str :
                if i[j].isalnum() :
                    l3.append(i[j])
    if type(i) == str :
        if i.isalnum() :
            l3.append(i)
print(l3)


# In[15]:


for i in l :
    mul = 1
    if type(i) == list or type(i) == tuple or type(i) == set :
        for j in i :
            if type(j) == int :
                mul = mul * j
    if type(j) == int :
        print(mul)


# In[16]:


l2 = []
for i in l :
    if type(i) == list or type(i) == dict or type(i) == set or type(i) == tuple :
        for j in i :
            l2.append(j)
    if type(i) == dict :
        for j in i :
            l2.append(i[j])
print(l2)


# In[ ]:




