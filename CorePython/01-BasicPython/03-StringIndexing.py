Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = "Hello Python"
>>> a[0]
'H'
>>> a[1]
'e'
>>> a[0] = "B"
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[0] = "B"
TypeError: 'str' object does not support item assignment
>>> a[0]
'H'
>>> a[0:4]
'Hell'
>>> a[0:5]
'Hello'
>>> a[-1]
'n'
>>> a[-2]
'o'
>>> a[:5]
'Hello'
>>> a[5:]
' Python'
>>> a[1:100]
'ello Python'
>>> a[100]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[100]
IndexError: string index out of range
>>> a[0:-1]
'Hello Pytho'
>>> a[::-1]
'nohtyP olleH'
>>> a[0::2]
'HloPto'
>>> a
'Hello Python'
>>> a[0:10:3]
'HlPh'
>>> len(a)
12
>>> 
