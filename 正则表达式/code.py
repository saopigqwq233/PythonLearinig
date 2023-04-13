import re

# 这是直接查找模式
mo1 = re.compile('Batman')
name1 = mo1.search('My favorite hero is Batman')
print(name1.group())

# 这是管道模式，可在||间隔元素中选择匹配
mo2 = re.compile('Batman|Superman')
name2 = mo2.search('My favorite hero is Superman')
print(name2.group())

# 管道分组模式，上部分代码优化
mo3 = re.compile('(Bat|Super|Spider)man')
name3 = mo3.search('My favorite hero is Spiderman')
print(name3.group())
print(name3.group(0))  # 0默认是整个匹配的字符串
print(name3.group(1))  # 1是匹配的第一个分组

# 管道模式只匹配第一个出现的
mo4 = re.compile('(Bat|Super)man')
name4 = mo4.search('I love Superman and Batman')
print(name4.group())  # 只输出第一个出现的Superman

# 字符直接查找模式
mo5 = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
phonenumber1 = mo5.search('我的电话号码是15600000000')
print(phonenumber1.group())

# 可有可无模式
mo6 = re.compile(r'(\+86)?(\d\d\d)(\d\d\d\d)(\d\d\d\d)')
phonenumber2 = mo6.search('他输入了+8615600000000到电话框')
phonenumber3 = mo6.search('另一个人输入18900000000')
print(phonenumber2.group())
print(phonenumber3.group())

# 就是要有特殊字符，比如(),\+
mo7 = re.compile('')