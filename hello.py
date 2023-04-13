Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print(good)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(good)
NameError: name 'good' is not defined
good=1
print(good)
1
print(2**6)
64
>>> 22//6
3
>>> 22**2//6
80
>>> 22**2
484
>>> 484//6
80
>>> 7+*3
SyntaxError: invalid syntax
>>> a=7+/3
SyntaxError: invalid syntax
>>> a=10
>>> a+=3
>>> print(a)
13
>>> print("aa")
aa
>>> print('aa')
aa
>>> print('aa'+a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print('aa'+a)
TypeError: can only concatenate str (not "int") to str
>>> print('aa%d',a)
aa%d 13
>>> print("good"*3)
goodgoodgood
>>> print("good "*3)
good good good 
>>> print("good\n")
good

>>> #这是注释
>>> myname=input()
刘文淏
>>> print("你好"+myname)
你好刘文淏
