#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1.Write a Python program to print "Hello Python"?

print('Hello Python')


# In[9]:


# 2.Write a Python program to do arithmetical operations addition and division.?

# Addition
add = 3 + 4
print(add)

# Addtion through user input

print('Additon')
a = int(input('Enter your first number: '))
b = int(input('Enter your second number: '))
addition = a + b
print(addition)

# Divsion 

divide = 4//2  
divide2 = 4/2  # it will give floating point number
print(divide, divide2)

# Division through user input

print('Division')
x = int(input('Enter your first number: '))
y = int(input('Enter your second number: '))
division = x/y
print(division)


# In[16]:


# 3.Write a Python program to find the area of a triangle?

base = int(input('Enter the value of base: '))
height = int(input('Enter the value of height: '))

area = 1/2*(base*height)     #area of triange formula (half of base*height)

print(area)


# In[32]:


# 4.Write a Python program to swap two variables?

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))
print('Before swapping a:',a,'b:',b)

a,b = b,a # swapping 

print('After swapping a:',a,'b:',b)


# In[28]:


# 5.Write a Python program to generate a random number?

import random       # import random module it will help us to genrate random number

random_number = random.randint(0,100)   # in this function we have to give a range and it will give output in this range.
print(random_number)                     # When we execute this program so we will get random number in b/w 0-100 on everytime.


# In[ ]:




