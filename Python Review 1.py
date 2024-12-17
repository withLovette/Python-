#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1.Numeric Types
#    1.Create variables my_int, my_float, and my_complex with the following values: 
#       my_int = 10 (integer) 
#       my_float = 3.14 (float) 
#       my_complex = 2 + 3j (complex number) 
#   2. Print the type of each variable using type(). 
#   3. Try adding my_int and my_float. What is the result? 
#   4. Multiply my_float by my_complex and print the result.


# In[5]:


#1
my_int = 10 
my_float = 3.14
my_complex = 2 + 3j


# In[56]:


#2
print(type(my_int))
print(type(my_float))
print(type(my_complex))   


# In[13]:


#3
print(my_int + my_float)


# In[14]:


#4
print(my_float * my_complex)


# In[15]:


# 2. Text Type 
#    1. Create a variable greeting and assign it the value "Hello, Python!". 
#    2. Print the type of the greeting variable. 
#    3. Extract and print the word "Python" from the string using slicing ([]). 
#    4. Use the len() function to find the length of the string. 


# In[32]:


#1
my_text = "Hello, Python!"


# In[28]:


#2
print(type(my_text))


# In[34]:


#3
print(my_text[7:13])


# In[57]:


#4
len(my_text)


# In[19]:


# 3. Sequence Types
# List
# 1. Create a list named my_list with these values: [1, 2, 3, 4, 5].
# 2. Print the type of my_list.
# 3. Print the first and last items in the list.
# 4. Change the second item in the list to 10 and print the updated list.


# In[20]:


#1
my_list = [1, 2, 3, 4, 5]


# In[21]:


#2
print(type(my_list))


# In[41]:


#3
print(my_list[0])    
print(my_list[-1]) 


# In[44]:


#4
my_list[1] = 10
print(my_list)


# In[22]:


# Tuple
# 1. Create a tuple named my_tuple with these values: (1, 2, 3, 4, 5).
# 2. Print the type of my_tuple.
# 3. Access and print the third item in the tuple.
# 4. Try to change the first item to 10. What happens?


# In[26]:


#1
my_tuple = (1, 2, 3, 4, 5)


# In[27]:


#2
print(type(my_tuple))


# In[52]:


#3
print(my_tuple[2])


# In[48]:


#4
my_tuple[0] = 10

#It threw an error. TypeError: 'tuple' object does not support item assignment


# In[25]:


# Range
# 1. Create a range object named my_range that includes numbers from 0 to 5.
# 2. Convert my_range to a list and print it.
# 3. Print the type of my_range.


# In[55]:


my_range = range(0, 5)
print(my_range) 


# In[60]:


print(list(my_range))


# In[61]:


print(type(my_range))


# In[62]:


# 4. Mapping Type
#    1. Create a dictionary named my_dict with the following key-value pairs:
#    'name': 'Alice'
#    'age': 25
#    'is_student': True
#    2. Print the type of my_dict.
#    3. Access and print the value of the 'name' key.
#    4. Add a new key 'grade' with the value 'A' and print the updated dictionary.


# In[63]:


#1
my_dict = {'name': 'Alice', 'age': 25, 'is_student': True}


# In[65]:


#2
print(type(my_dict))


# In[67]:


#3
print(my_dict['name'])


# In[70]:


#4
my_dict['grade'] = 'A'
print(my_dict)


# In[ ]:


# 5. Set Types
# Set
# 1. Create a set named my_set with the values {1, 2, 3, 4, 5}.
# 2. Print the type of my_set.
# 3. Try adding a duplicate value (e.g., 2) to the set. What happens?
# 4. Remove an item from the set (e.g., 3) and print the updated set.

# Frozenset
# 1. Create a frozenset named my_frozenset with the values {10, 20, 30}.
# 2. Print the type of my_frozenset.
# 3. Try to add a new value to the frozenset. What happens?


# In[92]:


# Set
#1
my_set = {1,2,3,4,5}


# In[93]:


#2
print(my_set)


# In[94]:


my_set.add(2)
print(my_set)

#There were no changes to the set, when duplicates are added


# In[95]:


my_set.remove(3)
print(my_set)


# In[96]:


# Frozenset
#1
my_frozenset = frozenset({10, 20, 30})
print(type(my_frozenset))


# In[98]:


my_frozenset.add(40)
print(my_frozenset)

#It threw an error. AttributeError: 'frozenset' object has no attribute 'add'


# In[74]:


# 6. Boolean Type
# 1. Create a variable is_python_fun and assign it the value True.
# 2. Create another variable is_java_fun and assign it the value False.
# 3. Print the type of both variables.
# 4. Use a print statement to show the result of the following expressions:
# o 5 > 3
# o 5 == 10
# o 5 < 3


# In[99]:


is_python_fun = True


# In[100]:


is_java_fun = False


# In[102]:


print(type(is_python_fun))
print(type(is_java_fun))


# In[104]:


print(5>3)
print(5==10)
print(5<3)


# In[ ]:




