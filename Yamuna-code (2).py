#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def word(s):
    if len(set(s))==1:
        return("no answer")
    else:
        for i in range(len(s)-1,0,-1):
           if s[i]>s[i-1]:
               one=s[:i]
               two=s[i:]
               break
               two=list(sorted(two))
        for i in range(len(two)):
           if one[-1]<two[i]:
               temp=one[-1]
               one[-1]=two[i]
               two[i]=temp
               break
        return("".join(one+two))
n=int(input())
for i in range(n):
           s=list(input())
           print(word(s))


# In[ ]:




