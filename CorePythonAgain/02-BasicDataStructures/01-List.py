Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5,"Hello","Bye",True]
>>> print(a)
[1, 2, 3, 4, 5, 'Hello', 'Bye', True]
>>> a.append(12)
>>> a
[1, 2, 3, 4, 5, 'Hello', 'Bye', True, 12]
>>> a.append("Python")
>>> a
[1, 2, 3, 4, 5, 'Hello', 'Bye', True, 12, 'Python']
>>> a.append('a','e','i','o','u')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a.append('a','e','i','o','u')
TypeError: append() takes exactly one argument (5 given)
>>> a.append(['a','e','i','o','u'])
>>> a
[1, 2, 3, 4, 5, 'Hello', 'Bye', True, 12, 'Python', ['a', 'e', 'i', 'o', 'u']]
>>> a[-1]
['a', 'e', 'i', 'o', 'u']
>>> a.pop()
['a', 'e', 'i', 'o', 'u']
>>> a
[1, 2, 3, 4, 5, 'Hello', 'Bye', True, 12, 'Python']
>>> a.pop(5)
'Hello'
>>> a
[1, 2, 3, 4, 5, 'Bye', True, 12, 'Python']
>>> vow = ['a', 'e', 'i', 'o', 'u']
>>> a.extend(vow)
>>> a
[1, 2, 3, 4, 5, 'Bye', True, 12, 'Python', 'a', 'e', 'i', 'o', 'u']
>>> a.insert(2,"Robot")
>>> a
[1, 2, 'Robot', 3, 4, 5, 'Bye', True, 12, 'Python', 'a', 'e', 'i', 'o', 'u']
>>> a.remove(True)
>>> a
[2, 'Robot', 3, 4, 5, 'Bye', True, 12, 'Python', 'a', 'e', 'i', 'o', 'u']
>>> a.remove("Robot")
>>> a
[2, 3, 4, 5, 'Bye', True, 12, 'Python', 'a', 'e', 'i', 'o', 'u']
>>> a.remove()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a.remove()
TypeError: remove() takes exactly one argument (0 given)
>>> a.remove(True)
>>> a
[2, 3, 4, 5, 'Bye', 12, 'Python', 'a', 'e', 'i', 'o', 'u']
>>> a.clear()
>>> a
[]
>>> a = [12,22,1,4,45,23,78,32,15,8]
>>> sorted(a)
[1, 4, 8, 12, 15, 22, 23, 32, 45, 78]
>>> sorted(a, reversed = True)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sorted(a, reversed = True)
TypeError: 'reversed' is an invalid keyword argument for this function
>>> sorted(a, reverse = True)
[78, 45, 32, 23, 22, 15, 12, 8, 4, 1]
>>> len(a)
10
>>> a = ['Ram', 'Shyam', 'Amit', 'Akash', 'Pooja', 'Ravi', 'Zoya', 'Bhanu']
>>> sorted(a)
['Akash', 'Amit', 'Bhanu', 'Pooja', 'Ram', 'Ravi', 'Shyam', 'Zoya']
>>> sorted(a, reverse = True)
['Zoya', 'Shyam', 'Ravi', 'Ram', 'Pooja', 'Bhanu', 'Amit', 'Akash']
>>> name = 'Ravi'
>>> name in a
True
>>> name not in a
False
>>> a = [12,18,1,"Hi", "Hello", "Python"]
>>> b = a
>>> b
[12, 18, 1, 'Hi', 'Hello', 'Python']
>>> a
[12, 18, 1, 'Hi', 'Hello', 'Python']
>>> b[2] = 100
>>> b
[12, 18, 100, 'Hi', 'Hello', 'Python']
>>> a
[12, 18, 100, 'Hi', 'Hello', 'Python']
>>> id(a)
2515053367368
>>> id(b)
2515053367368
>>> a[0:3] = 99,98,100
>>> a
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> a
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> b
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> b = a[:]
>>> b
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> a
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> b[0] = "Red"
>>> b
['Red', 98, 100, 'Hi', 'Hello', 'Python']
a
>>> a
[99, 98, 100, 'Hi', 'Hello', 'Python']
>>> id(a)
2515053367368
>>> id(b)
2515053367432
>>> a = [99, 98, 100, 'Hi', ['Ram', 'Shyam', 'Mohan'] 'Hello', 'Python']
SyntaxError: invalid syntax
>>> a = [99, 98, 100, 'Hi', ['Ram', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a
[99, 98, 100, 'Hi', ['Ram', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a[5]
'Hello'
>>> a[4]
['Ram', 'Shyam', 'Mohan']
>>> a[4][0]
'Ram'
>>> b = a[:]
>>> b
[99, 98, 100, 'Hi', ['Ram', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a[4][0] = "Ravi"
>>> a
[99, 98, 100, 'Hi', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> b
[99, 98, 100, 'Hi', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a[3]
'Hi'
>>> a[3] = 'Bye'
>>> a
[99, 98, 100, 'Bye', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> b
[99, 98, 100, 'Hi', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> import deepcopy
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    import deepcopy
ModuleNotFoundError: No module named 'deepcopy'
>>> import copy
>>> b = copy.deepcopy(a)
>>> b
[99, 98, 100, 'Bye', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a
[99, 98, 100, 'Bye', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> b[4][0] = 'Ram'
>>> b
[99, 98, 100, 'Bye', ['Ram', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> a
[99, 98, 100, 'Bye', ['Ravi', 'Shyam', 'Mohan'], 'Hello', 'Python']
>>> 
