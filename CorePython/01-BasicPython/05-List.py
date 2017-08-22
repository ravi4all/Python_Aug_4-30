Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5]
>>> type(a)
<class 'list'>
>>> a = [1,'Hi','Hello',10.5,True]
>>> print(a)
[1, 'Hi', 'Hello', 10.5, True]
>>> a = (1,2,3,4)
>>> type(a)
<class 'tuple'>
>>> a = 12,11,12
>>> type(a)
<class 'tuple'>
>>> a = {'id':1,"name":"Ram"}
>>> type(a)
<class 'dict'>
>>> a = [1,'Hi','Hello',10.5,True]
>>> a[0]
1
>>> a[1]
'Hi'
>>> a[3]
10.5
>>> a[-1]
True
>>> a[::-1]
[True, 10.5, 'Hello', 'Hi', 1]
>>> a[1:5]
['Hi', 'Hello', 10.5, True]
>>> a = (1,2,3,4)
>>> a[1]
2
>>> a[3]
4
>>> a[1:3]
(2, 3)
>>> list_1 = ['Hi',10,'Hello',10.5,True,11]
>>> tuple_1 = ('Hi',10,'Hello',10.5,True,11)
>>> list_1[2] = "Bye"
>>> list_1
['Hi', 10, 'Bye', 10.5, True, 11]
>>> tuple_1[2] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple_1[2] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> str = "Hello Python"
>>> str
'Hello Python'
>>> str = "Hello "Python""
SyntaxError: invalid syntax
>>> str = 'Hello "Python"'
>>> str
'Hello "Python"'
>>> var = "Hello"
>>> var in list_1
False
>>> var = "Hi"
>>> var in list_1
True
>>> list_1
['Hi', 10, 'Bye', 10.5, True, 11]
>>> tuple_1
('Hi', 10, 'Hello', 10.5, True, 11)
>>> list_1 == tuple_1
False
>>> list_2 = list_1
>>> list_1 == list_2
True
>>> list_1 is list_2
True
>>> list_2[0] = "Python"
>>> list_2
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_1
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_2 = list_1[:]
>>> list_2 is list_1
False
>>> list_2
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_1
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_2[0] = "Hi"
>>> list_2
['Hi', 10, 'Bye', 10.5, True, 11]
>>> list_1
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_1[:]
['Python', 10, 'Bye', 10.5, True, 11]
>>> list_1 == list_2
False
>>> id(list_1)
54589840
>>> id(list_2)
54575672
>>> list_2 = list_1
>>> id(list_1)
54589840
>>> id(list_2)
54589840
>>> list_2 = list_1[:]
>>> list_1.extend([99,98,97,96,95])
>>> list_1
['Python', 10, 'Bye', 10.5, True, 11, 99, 98, 97, 96, 95]
>>> list_2
['Python', 10, 'Bye', 10.5, True, 11]
>>> ['Python', 10, ['Bye', 10.5, True], 11, 99, 98, 97, 96, 95]
['Python', 10, ['Bye', 10.5, True], 11, 99, 98, 97, 96, 95]
>>> list_1[2][2]
'e'
>>> list_1[0]
'Python'
>>> list_1[2][3]
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    list_1[2][3]
IndexError: string index out of range
>>> list_1[2][1]
'y'
>>> list_1[2][0]
'B'
>>> list_1[2][3]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list_1[2][3]
IndexError: string index out of range
>>> for i in list_1:
	print(i)

	
Python
10
Bye
10.5
True
11
99
98
97
96
95
>>> list_1 = [10,"Hi", 11.5, ["Bye", True, 12], 99,100,102]
>>> list_1
[10, 'Hi', 11.5, ['Bye', True, 12], 99, 100, 102]
>>> list_1[3]
['Bye', True, 12]
>>> list_1[3][0]
'Bye'
>>> list_1[3][1]
True
>>> for i in list_1:
	print(i)

	
10
Hi
11.5
['Bye', True, 12]
99
100
102
>>> list_2 = list_1[:]
>>> list_2
[10, 'Hi', 11.5, ['Bye', True, 12], 99, 100, 102]
>>> list_1[0] = "Python"
>>> list_1
['Python', 'Hi', 11.5, ['Bye', True, 12], 99, 100, 102]
>>> list_2
[10, 'Hi', 11.5, ['Bye', True, 12], 99, 100, 102]
>>> list_2[3][0] = "Welcome"
>>> list_2
[10, 'Hi', 11.5, ['Welcome', True, 12], 99, 100, 102]
>>> list_1
['Python', 'Hi', 11.5, ['Welcome', True, 12], 99, 100, 102]
>>> import copy
>>> pygame.init()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    pygame.init()
NameError: name 'pygame' is not defined
>>> import pygame
>>> pygame.init()
(6, 0)
>>> import pygame
>>> list_2 = copy.deepcopy(list_1)
>>> list_2[3][0] = "Hulk"
>>> list_2
['Python', 'Hi', 11.5, ['Hulk', True, 12], 99, 100, 102]
>>> list_1
['Python', 'Hi', 11.5, ['Welcome', True, 12], 99, 100, 102]
>>> 
