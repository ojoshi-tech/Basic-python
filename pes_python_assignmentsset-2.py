#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import random
n= 0.543
round(n)


# In[2]:


n=841
math.sqrt(n)


# In[3]:


random.random()


# In[4]:


random.uniform(10,500)


# In[5]:


x = int(input("Enter a first value:"))
y = int(input("Enter a second value:"))
print("sin({})={}".format(x,math.sin(x)))
print("sin({})={}".format(y,math.sin(y)))
print("cos({})={}".format(x,math.cos(x)))
print("cos({})={}".format(y,math.cos(y)))
print("tan({})={}".format(x,math.tan(x)))
print("tan({})={}".format(y,math.tan(y)))


# In[6]:


def Area_circle(r):
    return (math.pi*(r**2))
R=int(input("Enter the radious: "))
print("Area of a circle is %d"%Area_circle(R))


# In[7]:


txt1 = 'It\'s alright.'
print(txt1) 
txt2 = "This will insert one \\ (backslash)."
print(txt2)
txt3 = "Hello\nWorld!"
print(txt3) 
txt = "Hello\tWorld!"
print(txt) 


# In[8]:


a=35.567
print("The temperature today is %d degrees outside !"%a)
print("The temperature today is %f degrees outside !"%a)
print ("This article is written in {}".format("Python")) 
print ("This is {} {} {} {}".format("one", "two", "three", "four"))
print("Every {3} should know the use of {2} {1} programming and {0}".format("programmer", "Open", "Source", "Operating Systems"))


# In[12]:


mystr = "malayalam"
mystr = mystr.lower()
rev_str = reversed(mystr)
if list(mystr)==list(rev_str):
    print("%s is a Palindrome"%mystr)
else:
    print("%s is not a Palindrome"%mystr)


# In[29]:


mystr = "This is Python"
mystr = mystr.lower()
count=0
my_dict = {}.fromkeys(['a','e','i','o','u'],0)
#print(mystr)
for x in mystr:
    #print(x)
    if x in my_dict:
        my_dict[x] +=1
        count +=1
print(my_dict)
print("Total number of Voals = %d"%count)


# In[36]:


mystr = "hello, and welcome to my world."
print(mystr.capitalize())#Converts the first character to upper case
print(mystr.casefold())#Converts string into lower case
txt = "banana"
x = txt.center(20, "O")
print(x)
txt1 = "I love apples, apple are my favorite fruit"
x1 = txt1.count("apple")
print(x1)
txt2 = "My name is Ståle"
x2 = txt2.encode()
print(x2)


# In[41]:


txt = "Hello, welcome to my world."#Returns true if the string ends with the specified value
x = txt.endswith(".")
print(x)
txt1 = "Hello, welcome to my world."#Searches the string for a specified value and returns the position of where it was found
x1 = txt1.find("welcome")
print(x1)
txt2 = print("My name is {fname}, I'am {age}".format(fname = "John", age = 36))#Formats specified values in a string
txt3 = print("My name is {0}, I'am {1}".format("John",36))
txt4 = print("My name is {}, I'am {}".format("John",36))
txt5 = "Hello, welcome to my world."#Searches the string for a specified value and returns the position of where it was found
x5 = txt5.index("welcome")
print(x5)
txt6 = "Company12"#Returns True if all characters in the string are alphanumeric
x6 = txt6.isalnum()
print(x6)


# In[43]:


txt1 = "CompanyX"#Returns True if all characters in the string are in the alphabet
x1 = txt1.isalpha()
print(x1)
txt2 = "50800"#Returns True if all characters in the string are digits
x2 = txt2.isdigit()
print(x2)
txt3 = "Demo"#Returns True if the string is an identifier
x3 = txt3.isidentifier()
print(x3)
txt4 = "hello world!"#Returns True if all characters in the string are lower case
x4 = txt4.islower()
print(x4)
txt5 = "565543"#Returns True if all characters in the string are numeric
x5 = txt5.isnumeric()
print(x5)


# In[47]:


txt1 = "hello only" #Returns True if all characters in the string are printable
x1 = txt.isprintable()
print(x1)

txt2 = "My world"#Returns True if all characters in the string are whitespaces
x2 = txt.isspace()
print(x2)

txt3 = "Hello, And Welcome To My World!" #Returns True if all characters in the string are whitespaces
x3 = txt.istitle()
print(x3)

txt4 = "Hello, And Welcome To My World!"#Returns True if the string follows the rules of a title
x4 = txt.istitle()
print(x4)

txt5 = "THIS IS NOW!" #Returns True if all characters in the string are upper case
x5 = txt.isupper()
print(x5)


# In[49]:


myTuple1 = ("John", "Peter", "Vicky") #Joins the elements of an iterable to the end of the string
x1 = "#".join(myTuple1)
print(x1)

txt2 = "banana"   #Returns a left justified version of the string
x2 = txt.ljust(20)
print(x2, "is my favorite fruit.")


# In[ ]:




