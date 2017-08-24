Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def func1():
	return "Hello world"

>>> def func2(func1):
	return func1

>>> a = func2(" ")
>>> a
' '
>>> a = func2()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a = func2()
TypeError: func2() missing 1 required positional argument: 'func1'
>>> a = func2(func1)
>>> a
<function func1 at 0x03C14738>
>>> print(a)
<function func1 at 0x03C14738>
>>> def parent():
	x = 10
	def child():
		x += 1
		print(x)

>>> parent()
>>> child()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    child()
NameError: name 'child' is not defined
>>> def parent():
	x = 10
	def child():
		x += 1
		print(x)
	child()

	
>>> parent()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    parent()
  File "<pyshell#23>", line 6, in parent
    child()
  File "<pyshell#23>", line 4, in child
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def parent():
	x = 10
	def child():
		x += 1
		print(x)
	return child

>>> parent()
<function parent.<locals>.child at 0x03C19DF8>
>>> a = parent()
>>> a
<function parent.<locals>.child at 0x03C19F18>
>>> a()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a()
  File "<pyshell#26>", line 4, in child
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> def parent():
	x = 10
	def child():
		x += 1
		print(x)
	return child()

>>> parent()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    parent()
  File "<pyshell#32>", line 6, in parent
    return child()
  File "<pyshell#32>", line 4, in child
    x += 1
UnboundLocalError: local variable 'x' referenced before assignment
>>> 
