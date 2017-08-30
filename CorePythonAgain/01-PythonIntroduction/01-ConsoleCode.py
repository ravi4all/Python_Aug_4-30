Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> a
10
>>> print(a)
10
>>> a = "Hello"
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = 10
>>> b = 20
>>> a+b
30
>>> id(a)
1650247632
>>> a = 12
>>> b = 11
>>> a/b
1.0909090909090908
>>> a*b
132
>>> a-b
1
>>> a//b
1
>>> a*a
144
>>> a*a*a
1728
>>> a**78
1500158654173824244445901346699938405046228479331843405109463057079932580570809237504
>>> a = "Hello Python"
>>> type(a)
<class 'str'>
>>> print(a)
Hello Python
>>> a
'Hello Python'
>>> a = 'Hello Python'
>>> a
'Hello Python'
>>> print(a)
Hello Python
>>> a = "Hello "Python""
SyntaxError: invalid syntax
>>> a = "Hello 'Python'"
>>> a
"Hello 'Python'"
>>> print(a)
Hello 'Python'
>>> a = 'Hello "Python"'
>>> print(a)
Hello "Python"
>>> a = "Hello \"Python""
SyntaxError: EOL while scanning string literal
>>> print(r"Hello \"Python"")
      
SyntaxError: EOL while scanning string literal
>>> print("Hello 'Python"')
      
SyntaxError: EOL while scanning string literal
>>> print("Hello 'Python'")
Hello 'Python'
>>> print("Hello \nPython")
Hello 
Python
>>> print(r"Hello \nPython")
Hello \nPython
>>> print("He's a boy")
He's a boy
>>> print("'He's a boy'")
'He's a boy'
>>> print('He's a boy')
      
SyntaxError: invalid syntax
>>> print('He"'"s a boy')
      
SyntaxError: EOL while scanning string literal
>>> print('He\'s a boy')
He's a boy
>>> 
