Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=' python '
b=a.rstrip()
a
' python '
b
' python'
a.strip()
'python'
a='you can \"do what you can\" in any con '
a
'you can "do what you can" in any con '
a.rstrip()
'you can "do what you can" in any con'
a.lstrip()
'you can "do what you can" in any con '
f"\"{a}\" is a message"
'"you can "do what you can" in any con " is a message'
"hello\n"
'hello\n'
f"hello\nyou"
'hello\nyou'
r"hello\nyou"
'hello\\nyou'
"hello\n"
'hello\n'
'you \n nothon'
'you \n nothon'
print('you \n nothon')
you 
 nothon
a='you \n nothing'
print(a)
you 
 nothing
print(f"{a}")
you 
 nothing
print(r'{a}')
{a}
print(r a)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
name_list=['ZhaoWenRui','Yangzhihao','Wangyuanqiu','Wangkaiqing']
print(name_list)
['ZhaoWenRui', 'Yangzhihao', 'Wangyuanqiu', 'Wangkaiqing']
print(name_list[2:3])
['Wangyuanqiu']
print(name_list[0:3])
['ZhaoWenRui', 'Yangzhihao', 'Wangyuanqiu']
print(name_list[1:3])
['Yangzhihao', 'Wangyuanqiu']
print(namey_list[0:2:1])
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(namey_list[0:2:1])
NameError: name 'namey_list' is not defined. Did you mean: 'name_list'?
print(name_list[0:2:1])
['ZhaoWenRui', 'Yangzhihao']
b=name_list[:]
b
['ZhaoWenRui', 'Yangzhihao', 'Wangyuanqiu', 'Wangkaiqing']
b.append('ye')
for name in b:
    print(f"{name} is my good friend\n")
    print('I respect him')

ZhaoWenRui is my good friend

I respect him
Yangzhihao is my good friend

I respect him
Wangyuanqiu is my good friend

I respect him
Wangkaiqing is my good friend

I respect him
ye is my good friend

I respect him
for name in b:
    print(f'{name} is my good friend',end='')
    print('\nI respect them')

ZhaoWenRui is my good friend
I respect them
Yangzhihao is my good friend
I respect them
Wangyuanqiu is my good friend
I respect them
Wangkaiqing is my good friend
I respect them
ye is my good friend
I respect them
len(b)
5
\
b.insert(2,'fuck u')
b
['ZhaoWenRui', 'Yangzhihao', 'fuck u', 'Wangyuanqiu', 'Wangkaiqing', 'ye']
a='woaini'
b.insert(4,a)
b
['ZhaoWenRui', 'Yangzhihao', 'fuck u', 'Wangyuanqiu', 'woaini', 'Wangkaiqing', 'ye']
b[4]
'woaini'
b[5]
'Wangkaiqing'
del b[b.index('ye')]
b
['ZhaoWenRui', 'Yangzhihao', 'fuck u', 'Wangyuanqiu', 'woaini', 'Wangkaiqing']
c=b.pop()
c
'Wangkaiqing'
c=b.pop(b.index('Yangzhihao'))
c
'Yangzhihao'
b
['ZhaoWenRui', 'fuck u', 'Wangyuanqiu', 'woaini']
b.sorted()
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    b.sorted()
AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?
sorted(b)
['Wangyuanqiu', 'ZhaoWenRui', 'fuck u', 'woaini']
b.lower()
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b.lower()
AttributeError: 'list' object has no attribute 'lower'
low(b)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    low(b)
NameError: name 'low' is not defined. Did you mean: 'pow'?
for i in range(5)
SyntaxError: incomplete input
for i in range(5):
    print(i)

0
1
2
3
4
>>> range(5)
range(0, 5)
>>> a=range(5)
>>> a
range(0, 5)
>>> for c in a:
...     print(c)
... 
0
1
2
3
4
>>> a[3]
3
>>> a[1]
1
>>> a[2]=1
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a[2]=1
TypeError: 'range' object does not support item assignment
>>> a[2]=2
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a[2]=2
TypeError: 'range' object does not support item assignment
>>> a[2]
2
>>> a=[]
>>> if a:
...     print('no')
... else:
...     print('empty')
... 
empty
