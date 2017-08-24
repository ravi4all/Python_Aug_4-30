Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num_1 =input("Enter first num: ")
Enter first num: 12
>>> num_2 = input("Enter second num : ")
Enter second num : 13
>>> result = num_1 + num_2
>>> print(result)
1213
>>> result = int(num_1) + int(num_2)
>>> result
25
>>> from __future__ import braces
SyntaxError: not a chance
>>> def myFunc():
	print("My first Function")

	
>>> myFunc()
My first Function
>>> def func2(x):
	print(x)

	
>>> func2(10)
10
>>> def func2(x):
	print(x)

	
>>> a = func2(10)
10
>>> a
>>> type(a)
<class 'NoneType'>
>>> print(a)
None
>>> def func2(x):
	return x

>>> a = func2(10)
>>> a
10
>>> type(a)
<class 'int'>
>>> print(a)
10
>>> def func2():
	return 1,2,3,4,5

>>> a = func2()
>>> a
(1, 2, 3, 4, 5)
>>> for i in a:
	print(i)

	
1
2
3
4
5
>>> type(a)
<class 'tuple'>
>>> i,j,k,l,m = func2()
>>> i
1
>>> j
2
>>> k
3
>>> l
4
>>> m
5
>>> i,j,k
(1, 2, 3)
>>> def func3(name, age):
	print("Name is {} and age is {}".format(name, age))

	
>>> func3('Ram', 20)
Name is Ram and age is 20
>>> func3(name = 'Ram', age = 20)
Name is Ram and age is 20
>>> func3(age = 20, name = 'Ram')
Name is Ram and age is 20
>>> func3(20, Ram)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    func3(20, Ram)
NameError: name 'Ram' is not defined
>>> func3(20, 'Ram')
Name is 20 and age is Ram
>>> def func3(name, age, address):
	print("Name is {} and age is {}".format(name, age))
	print("Address is", address)

	
>>> def func3(name, age, *address):
	print("Name is {} and age is {}".format(name, age))
	print("Address is", address)

	
>>> func3('Ram', 20, 'Delhi', 'Punjab', 'Patna')
Name is Ram and age is 20
Address is ('Delhi', 'Punjab', 'Patna')
>>> a = ['Hi','Hello',10,11]
>>> b = ('Hi', 'Hello',10,11)
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> a[0] = 'Bye'
>>> a
['Bye', 'Hello', 10, 11]
>>> b[0] = 'Bye'
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    b[0] = 'Bye'
TypeError: 'tuple' object does not support item assignment
>>> dict_1 = {'id':101, 'name':'Ram', 'age':20}
>>> dict_1.keys()
dict_keys(['id', 'name', 'age'])
>>> dict_1.values()
dict_values([101, 'Ram', 20])
>>> dict_1.items()
dict_items([('id', 101), ('name', 'Ram'), ('age', 20)])
>>> for i in dict_1.items():
	print(i)

	
('id', 101)
('name', 'Ram')
('age', 20)
>>> dict_1['name']
'Ram'
>>> dict_1 = {'id':101, 'name':'Ram', 'age':20, 'address':['Address_1', 'Address_2', 'Address_3']}
>>> dict_1.values()
dict_values([101, 'Ram', 20, ['Address_1', 'Address_2', 'Address_3']])
>>> for i in dict_1.items():
	print(i)

	
('id', 101)
('name', 'Ram')
('age', 20)
('address', ['Address_1', 'Address_2', 'Address_3'])
>>> 
