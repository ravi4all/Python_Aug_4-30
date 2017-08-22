Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = []
>>> a.append("Hi")
>>> a
['Hi']
>>> a.append("True")
>>> a
['Hi', 'True']
>>> a.append(10.5,6,11)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.append(10.5,6,11)
TypeError: append() takes exactly one argument (3 given)
>>> a.append([10.5,6,11])
>>> a
['Hi', 'True', [10.5, 6, 11]]
>>> a.append(10.5)
>>> a
['Hi', 'True', [10.5, 6, 11], 10.5]
>>> a.append(100)
>>> a.pop()
100
>>> a
['Hi', 'True', [10.5, 6, 11], 10.5]
>>> a.pop(2)
[10.5, 6, 11]
>>> a
['Hi', 'True', 10.5]
>>> a.extend([99,98,97,96])
>>> a
['Hi', 'True', 10.5, 99, 98, 97, 96]
>>> a.index(99)
3
>>> len(a)
7
>>> a.remove('Hi')
>>> a
['True', 10.5, 99, 98, 97, 96]
>>> a.insert(0,"Hi")
>>> a
['Hi', 'True', 10.5, 99, 98, 97, 96]
>>> a.insert(3,"Hello")
>>> a
['Hi', 'True', 10.5, 'Hello', 99, 98, 97, 96]
>>> a.reverse()
>>> a
[96, 97, 98, 99, 'Hello', 10.5, 'True', 'Hi']
>>> for i in range(10,15):
	print(i)

	
10
11
12
13
14
>>> for i in range(5):
	input("Enter name : ")

	
Enter name : ram
'ram'
Enter name : shyam
'shyam'
Enter name : gopal
'gopal'
Enter name : mohan
'mohan'
Enter name : arjun
'arjun'
>>> names = []
>>> for i in range(5):
	name = input("Enter name : ")
	names.append(name)
	print("Names list : ",names)

	
Enter name : Ram
Names list :  ['Ram']
Enter name : Shyam
Names list :  ['Ram', 'Shyam']
Enter name : Gopal
Names list :  ['Ram', 'Shyam', 'Gopal']
Enter name : Mohan
Names list :  ['Ram', 'Shyam', 'Gopal', 'Mohan']
Enter name : Arjun
Names list :  ['Ram', 'Shyam', 'Gopal', 'Mohan', 'Arjun']
>>> names
['Ram', 'Shyam', 'Gopal', 'Mohan', 'Arjun']
>>> names[3]
'Mohan'
>>> sorted(names)
['Arjun', 'Gopal', 'Mohan', 'Ram', 'Shyam']
>>> sorted(names, reverse = True)
['Shyam', 'Ram', 'Mohan', 'Gopal', 'Arjun']
>>> names.clear()
>>> names
[]
>>> 
