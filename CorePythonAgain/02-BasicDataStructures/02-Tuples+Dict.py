Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = [1,2,3,4,5,"Hello"]
>>> b = (1,2,3,4,5,"Hello")
>>> a
[1, 2, 3, 4, 5, 'Hello']
>>> b
(1, 2, 3, 4, 5, 'Hello')
>>> type(a)
<class 'list'>
>>> type(b)
<class 'tuple'>
>>> a[-1]
'Hello'
>>> b[-1]
'Hello'
>>> a[0:3]
[1, 2, 3]
>>> b[0:4]
(1, 2, 3, 4)
>>> a[2] = "Hi"
>>> a
[1, 2, 'Hi', 4, 5, 'Hello']
>>> b[2] = "Hi"
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    b[2] = "Hi"
TypeError: 'tuple' object does not support item assignment
>>> emp = {'id':101, 'name':'Ram', 'Age':20}
>>> type(emp)
<class 'dict'>
>>> emp.keys()
dict_keys(['id', 'name', 'Age'])
>>> emp.values()
dict_values([101, 'Ram', 20])
>>> emp.items()
dict_items([('id', 101), ('name', 'Ram'), ('Age', 20)])
>>> for i in a:
	print(i)

	
1
2
Hi
4
5
Hello
>>> for i in b:
	print(i)

	
1
2
3
4
5
Hello
>>> for i in emp:
	print(i)

	
id
name
Age
>>> for i in emp.values():
	print(i)

	
101
Ram
20
>>> for i in emp.items():
	print(i)

	
('id', 101)
('name', 'Ram')
('Age', 20)
>>> 
