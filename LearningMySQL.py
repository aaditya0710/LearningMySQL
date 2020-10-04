#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector as sql
connection = sql.connect(host = "localhost",user="root",password= "12345",database="student")
print(connection)


# In[3]:


cursor = connection.cursor()

cursor.execute("CREATE TABLE studentinfo (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), subject VARCHAR(255) )")


# In[5]:


query = "INSERT INTO studentinfo (name,subject) VALUES (%s,%s)"
value = ('Aaditya','DBMS')
cursor.execute(query,value)
print("Row inserted", cursor.lastrowid)


# In[6]:


cursor = connection.cursor()
cursor.execute("Select * from studentinfo")


# In[7]:


cursor.fetchall()


# In[9]:


query = "INSERT INTO studentinfo (name,subject) VALUES (%s,%s)"
values = [("alex","data science"),
         ("smith","statistics"),
         ("david","machine learning")]
cursor.executemany(query,values)
print("Row inserted",cursor.lastrowid)


# In[18]:


cursor = connection.cursor()
cursor.execute("Select * from studentinfo")


# In[15]:


cursor.fetchall()


# In[19]:


for record in cursor.fetchall():
    print(record)


# In[20]:


cursor.execute("Select * from studentinfo where name='Aaditya'")


# In[21]:


cursor.fetchall()


# In[22]:


cursor.execute("SELECT DISTINCT subject from studentinfo")
cursor.fetchall()


# In[24]:


cursor.execute("SELECT name,subject from studentinfo where name='aaditya' or subject='data science' ")
cursor.fetchall()


# In[25]:


cursor.execute("DROP TABLE studentinfo")


# In[ ]:




