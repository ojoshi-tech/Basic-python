a=4
b=2
print(a+b,a-b,a*b,a/b)

-----------------------------------------------------------------------------------------

a=3683.7279
b=2317.6398
c=128.17401
if(a>b and a>c):
    print("Biggest Value is:%f"%a)
elif(b>a and b>c):
    print("Biggest Value is:%f"%b)
else:
    print("Biggest Value is:%f"%c)

-----------------------------------------------------------------------------------------


a=29
if (a%2==0):
    print("%d is even number"%a)
else:
          print("%d is odd number"%a)
    
  -----------------------------------------------------------------------------------------  
    
b=13
if (b%2==1):
    print("%d is a prime number"%b)
else:
    print("%d is not a prime number"%b)
    
  -----------------------------------------------------------------------------------------  
    
str = "Hello, World!"
sub1 = str[0:5]
print(sub1)
sub2 = str[:7]
print(sub2)
rep = sub1*100
print(rep)
sub3 = "Welcome to Python"+str[6:]
print(sub3)

-----------------------------------------------------------------------------------------

lst = [32,45,656,1,2,4,6,8,9,80]
print(lst)
print(lst[3:8])
print(lst*2)
lst2 = [1,2,3]
lst3 = lst + lst2
print(lst3)

-----------------------------------------------------------------------------------------

tup =(1,2,3,4,5,6,7,8,9,10)
print(tup)
print(tup[2:6])
print(tup*2)
print((tup,)*2)
tup1 = (454,85,64)
print(tup+tup1)

-----------------------------------------------------------------------------------------

c1 = 3 + 6j
c2 = 6 + 15j
print("Addition of two complex number =", c1 + c2)
print("Subtraction of two complex number =", c1 - c2)
print("Multiplication of two complex number =", c1 * c2)
print("Division of two complex number =", c1 / c2)

-----------------------------------------------------------------------------------------

a = 10
a += 3
print(a)
a -= 3
print(a)
a *=3
print(a)
a /= 2
print(a)
a %= 3
print(a)
a = 10 
a //= 2
print(a)
a **= 2
print(a)

-----------------------------------------------------------------------------------------
a= 10
b= 4
c= a & b
print(c)
d = a|b
print(d)
e = ~a
print(e)
f = a^b
print(f)

-----------------------------------------------------------------------------------------

lst = [int(i) for i in input("Enter 10 values seprating with space: ").split()]

avg = sum(lst)/5
print("Average =",avg)
count1 =0
for i in lst:
    if i > avg:
        count1 +=1
print("How many numbers are more than average :",count1)
count2 =0
for j in lst:
    if j == avg:
        count2 +=1
print("How many numbers are equal to average :",count2)


-----------------------------------------------------------------------------------------

p =int(input("Enter a first value :"))
q =int(input("Enter a second value :"))
r =int(input("Enter a third value :"))
s =int(input("Enter a forth value :"))
if p>=q and p>=r and p>=s:
    print("The biggest number is :",p)
elif q>=p and q>=r and q>=s:
    print("The biggest number is :",q)
elif r>=p and r>=q and r>=s:
    print("The biggest number is :",r)
elif s>=p and s>=q and s>=r:
    print("The biggest number is :",s)
    
 -----------------------------------------------------------------------------------------   
    
lstA = [1002,5689,2348,4379,8290,5678,3575,2468,5466,2376]
lstB = ['Onkar','Juilee','Ranjana','Ankit','Ram','Mahesh','Gaurav','Nikhil','Rajat','Surekha']

print(lstB)

o = int(input("Enter the index number to display name and ID :"))
print("Name =",lstB[o])
print("ID =",lstA[o])

print(lstB[4:10])

print(lstB[3:])

f = int(input("Enter the number to repeat list elements :"))
for ele in lstA:
    for i in range(f):
        print(ele)

print("Concatenated List")
print(lstA + lstB)

-----------------------------------------------------------------------------------------
name = ['Ram', 'Mahesh', 'Gaurav', 'Nikhil', 'Rajat']
exe = input("Enter the name you want to check :")
if exe in name:
    print("Given Name, %s Exsists"%exe)
else:
    print("Given Name, %s does not Exsists"%exe)

for ele in range(len(name)):
    if list(exe)==list(name[ele]):
        print("%s Name Exsists"%exe)
print("Given Name %s does not Exsists"%exe)
    
def Reverse(lst): 
    return [ele for ele in reversed(name)]
print(Reverse(name))

-----------------------------------------------------------------------------------------

num = int(input("Enter the number which you want to check :"))

if num > 1:  
    for i in range(2,num//2):   
        if (num % i) == 0: 
            print(num, "is not a prime number") 
            break
    else: 
        print(num, "is a prime number") 
else: 
    print(num, "is not a prime number") 
    
 -----------------------------------------------------------------------------------------   
    
a=324
b=876
if a>b:
    print("%d is greater then %d."%(a,b))
else:
    print("%d is greater then %d."%(b,a))
    
-----------------------------------------------------------------------------------------    
    
begin = int(input("Enter the first number of range:"))
end = int(input("Enter the last number of range:"))

for x in range(begin,end):
    print(x)
    
-----------------------------------------------------------------------------------------    

i = 1
while(i<=100):
    print(i)
    i += 1

-----------------------------------------------------------------------------------------
    
mystring ="Hello world"
for char in mystring:
    print(char)
    
 -----------------------------------------------------------------------------------------   
    
 for i in range (1,101):
  if i%2!=0:
    continue
  print (i)
 ----------------------------------------------------------------------------------------- 
  
for i in range(1,101):
    if i%2==0:
        if i==50:
            break
        else:
            print(i)
            
  -----------------------------------------------------------------------------------------          
            
for i in range(1,101):
    if i%2==0:
        if(i==10 or i==20 or i==30 or i==40 or i==50):
            continue
        print(i)


-----------------------------------------------------------------------------------------

i=1
while i<=100:
  if i%2!=0:
    i+=1
    continue
  print (i)
  i+=1
  
-----------------------------------------------------------------------------------------  
  
 i=1
while i<=100:
  if i==90:
    break
  print (i)
  i=i+1 

-----------------------------------------------------------------------------------------

i=1
while (i<=100):
  if (i==60 or i==70 or i==80 or i==90):
    i=i+1
    continue
  print (i)
  i=i+1

-----------------------------------------------------------------------------------------

num=int(input("Enter the no of terms"))
a=0 
b=1
if num<=0:
  print("please enter positive number")
elif num==1:
  print("Fibonacci series:",a)
elif num==2:
  print (a)
  print (b)
else:
  print (a)
  print (b)
  while(num>2):
    num1=a+b
    print (num1)
    a=b
    b=num1
    num=num-1
 -----------------------------------------------------------------------------------------   






