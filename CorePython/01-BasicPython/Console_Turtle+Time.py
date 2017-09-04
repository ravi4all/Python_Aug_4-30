Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello world")
Hello world
>>> a = 10
>>> type(a)
<class 'int'>
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = "10"
>>> a = 'Hello world'
>>> a = 'Hello "world"'
>>> a
'Hello "world"'
>>> print(a)
Hello "world"
>>> str = "Hello \nPython"
>>> str
'Hello \nPython'
>>> print(str)
Hello 
Python
>>> import random
>>> random.randint(0,100)
73
>>> random.randrange(0,100)
46
>>> a = [1,2,3,4,5,6,7]
>>> type(a)
<class 'list'>
>>> a = [1,"Hello",10.5,True]
>>> for i in a:
	print(i)

	
1
Hello
10.5
True
>>> import turtle
>>> myTurtle = turtle.Pen()
>>> myTurtle.shape("turtle")
>>> myTurtle.forward(150)
>>> myTurtle.left(90)
>>> myTurtle.forward(150)
>>> myTurtle.left(90)
>>> myTurtle.forward(150)
>>> myTurtle.left(90)
>>> myTurtle.forward(150)
>>> myTurtle.reset()
>>> for i in range(4):
	myTurtle.forward(150)
	myTurtle.left(90)

	
>>> myTurtle.reset()
>>> for i in range(20):
	myTurtle.forward(150)
	myTurtle.left(90+i*2)

	
>>> myTurtle.reset()
>>> for i in range(20):
	myTurtle.forward(150)
	myTurtle.left(90+i)

	
>>> myTurtle.reset()
>>> for i in range(20):
	myTurtle.circle(150)
	myTurtle.left(90)

	
Traceback (most recent call last):
  File "<pyshell#47>", line 2, in <module>
    myTurtle.circle(150)
  File "C:\Python36-32\lib\turtle.py", line 1993, in circle
    self._rotate(w)
  File "C:\Python36-32\lib\turtle.py", line 3278, in _rotate
    self._update()
  File "C:\Python36-32\lib\turtle.py", line 2663, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python36-32\lib\turtle.py", line 566, in _delay
    self.cv.after(delay)
  File "C:\Python36-32\lib\tkinter\__init__.py", line 741, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> myTurtle.reset()
>>> for i in range(20):
	myTurtle.circle(50)
	myTurtle.left(90+i*5)

	
>>> myTurtle.reset()
>>> myTurtle.speed(0)
>>> for i in range(20):
	myTurtle.circle(50)
	myTurtle.left(90+i*5)

	
>>> myTurtle.reset()
>>> color = ['red', 'green', 'blue']
>>> myTurtle.speed(0)
>>> for i in range(20):
	col = random.choice(color)
	myTurtle.color(col)
	myTurtle.circle(50)
	myTurtle.left(90+i*5)

	
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now)
2017-08-24 17:26:49.085784
>>> now.date
<built-in method date of datetime.datetime object at 0x03B37998>
>>> now.date()
datetime.date(2017, 8, 24)
>>> now.month
8
>>> now.day
24
>>> now.year
2017
>>> import calendar
>>> cal = calendar.month(2017, 8)
>>> print(cal)
    August 2017
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

>>> 
