Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def tempConv():
	return float(9/5 * c+32)

>>> cel = [34.5, 28.1, 39.3, 33.2, 37.5]
>>> f = map(tempConv, cel)
>>> f
<map object at 0x00000168E2DD3F98>
>>> f = list(map(tempConv, cel))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f = list(map(tempConv, cel))
TypeError: tempConv() takes 0 positional arguments but 1 was given
>>> def tempConv(c):
	return float(9/5 * c+32)

>>> f = list(map(tempConv, cel))
>>> f
[94.1, 82.58000000000001, 102.74, 91.76, 99.5]
>>> l = list(filter(tempConv, cel))
>>> l
[34.5, 28.1, 39.3, 33.2, 37.5]
>>> def even(e):
	return e%2 == 0

>>> num = [x for x in range(50)]
>>> num
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
>>> l = list(filter(ev, cel))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l = list(filter(ev, cel))
NameError: name 'ev' is not defined
>>> l = list(filter(even, num))
>>> l
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> l = list(map(even, num))
>>> l
[True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]
>>> a = lambda x,y : x + y
>>> type(a)
<class 'function'>
>>> 
