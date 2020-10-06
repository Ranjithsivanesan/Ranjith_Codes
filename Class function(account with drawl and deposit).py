#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Account():
    
    def __init__ (self,customer,balance):
        
        self.customer = customer
        self.balance = balance
      
    def deposit (self,dep_amnt):
        
        self.balance = self.balance + dep_amnt
        
    def withdrawl (self,with_amnt):
        
        if self.balance >= with_amnt:
            self.balance = self.balance - with_amnt
        else:
            print(f"your withdrawl of amount {with_amnt} is unsucessful as your balance is just {self.balance}")       
            


# In[37]:


a = Account("ranjith",500)


# In[38]:


a.customer


# In[39]:


a.balance


# In[40]:


a.deposit(300)


# In[41]:


a.balance


# In[42]:


a.withdrawl(900)


# In[43]:


a.deposit(100)


# In[44]:


a.withdrawl(900)


# In[45]:


a.balance


# In[ ]:





# In[ ]:




