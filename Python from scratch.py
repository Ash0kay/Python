#Learn python from sratch

"""
Topics
1. Primitive Datatypes & Operators
2. Variables & Collections
3. Control Flow & Iterables
4. Functinos
5. Modules
6. Class(oops)Inheritance
7. Some adance stuffs
"""
 
"""
1. Primitive Datatypes & Operators
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
B – Brackets/functions: Perform calculations inside brackets first (including parentheses (), square brackets [], and curly braces {}).
O – Orders/exponent: Refers to powers (exponents) and roots (like square roots).
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

_____________________________________________________________________________________________________________________________
   Int         | Float          | String                               | Lists          | Tuple | Dict | set|
   A:I D:I =I  |  A:I, D:I =I   | A:M(for Data) A:I(for Idns), D:I =I  | A:I D:M = M    |       |      |    |


Python memory management has static identifier for 256 numbers it will apply to alphabuts also 
so the address and value are immutable in int
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
# string
#in the below id will not be same
a= "hello world"
b= "hello world"
id(a)
id(b)
#in the below id will be same
a= "hello_world"
b= "hello_world"
id(a)
id(b)

"""
Data Types: (1-4 core or premitive data types, 5-8 are collections) All are OOPS(object oriented programming languages)
1. Integer(1,2,3,5,19)
2. Float(1.0,0.12,2.15)
3. Boolean(True, False)
4. String
5. Lists
6. Tuple
7.Dictonary
8. Set

NOTES: 
Looking at OOPS
What is OOPS? 

Object ->
      Members(variables/objects/properties)
      Methods(functions)


Strings("anything inside the double coutes are string")
      "this is single line  string" """
#' this is also string with single coutes'
      """ this is multiline string""" 
#if we assinged this multi line comments to an variable it will not considered as comment

DATE: 07-04-2025
Indexing
b= "hello world"
b[3] -> l
n[-2] -> l
 0  1  2 3 4 5 6 7 8 9 10
 h  e  l l o   w o r l d
-11 10 9 8 7 6 5 4 3 2 1


it will be "l" it can callout the index value of the string
it can be done forward and backword also
indexing principles are same across all the data type that uses index

name= "batman"
msg = f"bruce wyane is {name}"
msg
It will print "bruce wyane is batman" that f is formating and it will be avaiblae in only python 3.6 are above
 """"
 
 DATE: 08-04-2025
 How does a operater works on string
string concadination
 a= "hello"
 b= "world"
 c= a+b
 
"""
"""
DATE: 09-04-2025

How do find a functions in python
What is functions?
Functions is all about substituion


Print("hello world")
Anotony of a FN call
Funciton:name(""argument: string")
__________________________________________________________________________________________________________________
2. Variables and Collections
__________________________________________________________________________________________________________________

Variables: It is a container for storing values
Python will automatically determine the datatype
i= 5
i= "string"

#TIP: Decdocs.io  will help to learn python like a cheat code.
#try to refer with developer documentation for the rest of these modules so you can understand how the python or any other language works

CODE:
>>> s = 10 + 2
>>> s
12
>>> s = input("say your name? ")
say your name? test
>>> s
'test'
>>>

Collections: 

1. Lists
2. Tuples
3. Dictionary
4. Set





