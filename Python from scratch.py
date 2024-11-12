#Learn python from sratch

"""
Python is a interpereter high level language
- unlike other programming language python used to compile and run each line one by one Python’s syntax is clean and easy to understand, which makes it ideal for beginners 
and experienced developers alike.
- Python is a widely used programming language known for its simplicity and ease of learning. 
Its clean and readable syntax makes it great for beginners, while its powerful features attract experienced developers. 
Python is versatile and used for web development, data analysis, automation, and even game development.

- What makes Python stand out is its ability to run code without needing to compile it first, and you don’t have to declare variable types. 
Python also comes with many built-in libraries, making it easy to perform tasks like math, data analysis, or web development. 
Plus, it works on any platform, including Windows, Mac, and Linux.

- Compared to other languages, Python is much easier to learn and use than C/C++ or Java. 
It requires less code to achieve the same results, and it's great for both small scripts and large projects. 
Python’s large community means there's a wealth of resources and libraries available, making it perfect for everything from basic tasks to complex applications. 
"""
#Lets learn syntax in python
#arrithmetic operaters
# "+,-,*,/,//,%"
#addition +
a=5
b=5
c=a+b
print(c)
#subraction -
a=5
b=5
c=a-b
print(c)
#Multiplication * 
a=5
b=5
c=a*b
print(c)
#Division /
a=5
b=5
c=a/b
print(c)
#floor division //
a=5
b=5
c=a//b
print(c)
#Modulus %
a=5
b=5
c=a%b
print(c)
#Exponentiation **
a=5
b=5
c=a**b
print(c)

""" 
All the premitie operations will be calculated from the order of BODMAS
B – Brackets: Perform calculations inside brackets first (including parentheses (), square brackets [], and curly braces {}).
O – Orders: Refers to powers (exponents) and roots (like square roots).
D – Division: Perform division next, from left to right.
M – Multiplication: Perform multiplication next, from left to right.
A – Addition: Perform addition after multiplication and division, from left to right.
S – Subtraction: Perform subtraction after addition, from left to right.
"""

#Comparision operators:
"""
The output of the comparision operaters will be always boolean
== -> Equality (Equal to)
!= -> Inquality (not Equal to)
> -> Greater than
< -> Less than
>= -> Greater than or equal to
<= -> Less than or equal to 
All the above compare values
is -> check if both variables have same ref 
the "is" will compare id and it is specific to python
"""
# Chaning comparisions:
#Gates: When you want to apply multiple comparisions you need to apply gates
"""
Basic Logical Gates:
1. AND
2. OR
3. NOT

AND:  A B C
      0 0 0
      0.1.0
      1.0.0
      1.1.1
OR:
     A B C
     0 0 0
     0 1 1
     1 0 1
     1 1 1
NOT  A B 
     1 0
     0 1 
  """   
#4<6<9 Bassically if we didn't mentioned the and or gate it will take it as AND

# This is the Python marathon second part to learn from scratch
#Date 10-11-2024
''' The ID value will change once it reach the number of 256. it comes under memory management
why does it behaving like this?
Datatype memory management 
each datatypes will make a mynute change in in memory management datatypes like (int.flat,string,lists,tuple,dictnory,set)
 I - Immutable  (Data Types in python where the value assigned to a variable cannot be changed) if you cannot modify the data stored in the variable without modifying the 
 address it means the data type is imutable
 
 M - Mutable (Data types in python where the value assigned to a variable can be changed ) 
 if you can modify the data stored in the variable without modifying the address it means the datatype is mutable
 for example int is immutable and list is mutable

'''
#LIST (mutable)
a= [1,2,3,4]
id(a)
a.append(5)
id(a)
#int (immutable)
b=10
id(b)
b=b+1
id(b)
#Flot(immutable)
a =256.0
b= 256.0
id(a)
126344921958544
id(b)
126344921958736


"""
Data Types: 
Integer(1,2,3,5,19)
Float(1.0,0.12,2.15)
Boolean(True, False)
Strings("anything inside the double coutes are string")
      "this is single line  string" """
#' this is also string with single coutes'
      """ this is multiline string""" 
#if we assinged this multi line comments to an variable it will not considered as comment
  """
   
