Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a = "Hello"
>>> a = 'Hello'
>>> type(a)
<class 'str'>
>>> a
'Hello'
>>> a = 11
>>> type(a)
<class 'int'>
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a = 10.55555555555555555555555
>>> type(a)
<class 'float'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> a = "Hello"
>>> a*5
'HelloHelloHelloHelloHello'
>>> b = "World"
>>> a+b
'HelloWorld'
>>> a*5+
SyntaxError: invalid syntax
>>> a*5+"world"
'HelloHelloHelloHelloHelloworld'
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/01-PythonSyntax.py 
HelloWorld
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/01-PythonSyntax.py 
HelloWorld
30
>>> c
10
>>> a
'Hello'
>>> b
'World'
>>> c
10
>>> d
20
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/01-PythonSyntax.py 
HelloWorld
30
-10
0.5
200
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/01-PythonSyntax.py 
HelloWorld
10
10
Traceback (most recent call last):
  File "E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/01-PythonSyntax.py", line 10, in <module>
    print(c/d)
ZeroDivisionError: division by zero
>>> a = 12
>>> b = 13
>>> a/b
0.9230769230769231
>>> a//b
0
>>> b = 5
>>> a/b
2.4
>>> round(a/b)
2
>>> a//b
2
>>> a/b
2.4
>>> import math
>>> math.ceil(a/b)
3
>>> a = 23
>>> a*a
529
>>> a*a*a
12167
>>> a**5
6436343
>>> a = "hello"
>>> a.capitalize()
'Hello'
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/02-BasicStringFunctions.py 
RaviTyagi
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/02-BasicStringFunctions.py 
Ravi Tyagi
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/02-BasicStringFunctions.py 
Enter first name : ravi
Enter last name : tyagi
ravi tyagi
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/02-BasicStringFunctions.py 
Enter first name : ravi
Enter last name : tyagi
Ravi Tyagi
>>> 
 RESTART: E:/BMPL_Batches/Aug_2017/Regular/Python/Python_4-30-6_30/CorePython/01-BasicPython/02-BasicStringFunctions.py 
Enter first name : ravi
Enter last name : tyagi
ravi tyagi
Ravi Tyagi
RAVI TYAGI
>>> firstname
'ravi'
>>> firstname.lower()
'ravi'
>>> a = 'RaVi'
>>> a.swapcase()
'rAvI'
>>> isinstance(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    isinstance(a)
TypeError: isinstance expected 2 arguments, got 1
>>> isinstance(a, str)
True
>>> isinstance(a, int)
False
>>> isinstance(a, object)
True
>>> isinstance(str, object)
True
>>> type(str)
<class 'type'>
>>> type(None)
<class 'NoneType'>
>>> type(object)
<class 'type'>
>>> type(a)
<class 'str'>
>>> type(print)
<class 'builtin_function_or_method'>
>>> 
