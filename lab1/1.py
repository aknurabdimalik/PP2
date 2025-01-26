print("Hello, World!")

#2
import sys

print(sys.version)

#3
if 7 > 6:
  print("Seven is greater than six!")
if 7 > 6:
    print("Seven is greater than six!")

#4
x = 5
y = "Hello, World!"

print(x)
print(y)

#5

x = 5
y = "John"
print(x)
print(y)

#6
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#7
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#8
x = 5
y = "John"
print(type(x))
print(type(y))

#9
a = 4
A = "Sally"

print(a)
print(A)

#10
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#11
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#12
x = y = z = "Orange"
print(x)
print(y)
print(z)

#13
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#14
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#15
x = 5
y = 10
print(x + y)

#16
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#17
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#18
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#19
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#20
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#21
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#22
import random

print(random.randrange(1, 10))

#23
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

#24
a = "Hello, World!"
print(a[1])

#25
for x in "banana":
  print(x) 

#26
a = "Hello, World!"
print(len(a))

#27
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#28
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#29
b = "Hello, World!"
print(b[2:5])

#30
b = "Hello, World!"
print(b[-5:-2])


#31
a = "Hello, World!"
print(a.upper())
print(a.lower())

#32
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#33
txt = f"The price is {20 * 59} dollars"
print(txt)
