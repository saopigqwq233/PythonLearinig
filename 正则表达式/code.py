import re

# 这是直接查找模式
mo1 = re.compile('Batman')
name1 = mo1.search('My favorite hero is Batman')
print(name1.group())

# 这是管道模式，可在||间隔元素中选择匹配
mo2 = re.compile(r'Batman|Superman')
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
phone_number1 = mo5.search('我的电话号码是15600000000')
print(phone_number1.group())
# 分组模式
mo5 = re.compile(r'(\+86)(\d\d\d)(\d\d\d\d)(\d\d\d\d)')
phone_number1 = mo5.search('我的电话号码是+8618900000000')
print('电话号码'+phone_number1.group())
print('前缀'+phone_number1.group(1))

# 可有可无模式
import re
mo6 = re.compile(r'(\+86)?(\d\d\d)(\d\d\d\d)(\d\d\d\d)')
phone_number2 = mo6.search('他输入了+8615600000000到电话框')
phone_number3 = mo6.search('另一个人输入18900000000')
print(phone_number2.group())
print(phone_number3.group())

# 就是要有特殊字符，比如(),\+
import re
mo7 = re.compile(r'(\(\+\d\d\))(\d\d\d)(\d\d\d\d)(\d\d\d\d)')
phone_number4 = mo7.search('我的电话号码是(+86)15600000000')
print(phone_number4.group())

# 匹配任意数量的字符
import re
mo8 = re.compile(r'\d*%')
money = mo8.search('本期涨幅有143%')
print(money.group())
money = mo8.search('本期涨幅为?%')
print(money.group())

# 匹配任意数量存在的字符
import re
mo9 = re.compile(r'\d+')
numbers = mo9.search('第一产业增加值54779亿元')
print(numbers.group())
# 未出现会怎么样
mo9 = re.compile(r'\d+亿元')
numbers = mo9.search('第一产业增加值????亿元')
print(type(numbers))

# 匹配指定次数
mo10 = re.compile(r'(\+\d\d)?(\d){11}')
phone_number5 = mo10.search('电话号码是15600000000')
print(phone_number5.group())

# 匹配范围次数
mo11 = re.compile(r'\+?\d{11,13}')
phone_number6 = mo11.search('电话号码是+8615600000000')
print(phone_number6.group())

# 贪心匹配方式
mo12 = re.compile(r'\d{3,5}')
num1 = mo12.search('数字有34567')
print(num1.group())  # 匹配最多的数字

# 非贪心匹配
mo13 = re.compile(r'\d{3,5}?')
num2 = mo13.search('数字有34567')
print(num2.group())  # 匹配最少的数字

# 返回匹配的所有文本,返回一个字符串列表
mo14 = re.compile(r'\d{11}')
phone_number7 = mo14.findall('电话号码1：15600000000'
                             '电话号码2：19100000000'
                             '电话号码3：18700000000')
print(phone_number7)

# 如果加了分组，则返回元组的列表，元组内是匹配项分组字符串
mo15 = re.compile(r'(\d{3})(\d{4})(\d{4})')
phone_number8 = mo15.findall('电话号码1：15600000000'
                             '电话号码2：19100000000'
                             '电话号码3：18700000000')
print(phone_number8)

# 自定义匹配字符模式
mo16 = re.compile(r'\b[aeiouAEIOU]\w*')
vowel_word = mo16.findall('I am obviously angry with you')
print(vowel_word)

# []内书写特殊字符时不需要加上\来进行转义
mo17 = re.compile(r'[*?+]+')
special_character = mo17.findall('*+?11*?')
print(special_character)

# 加上^则是不匹配这些,匹配其它所有字符类型
mo18 = re.compile(r'\b[^aeiouAEIOU\n\t ]\w*')
non_vowel_word = mo18.findall('I am obviously angry with you')
print(non_vowel_word)

# ^字符和$字符的作用
mo19 = re.compile(r'^(name):(\d)+')
name_phone1 = mo19.search('name:15600000000这是信息的格式')
print(name_phone1.group())
name_phone1 = mo19.search('信息的格式是name:15600000000')
print(type(name_phone1))

mo20 = re.compile(r'(name):(\d)+$')
name_phone2 = mo20.search('信息的格式是name:15600000000')
print(name_phone2.group())
name_phone2 = mo20.search('name:15600000000这是信息的格式')
print(type(name_phone2))

# 接收所有的  .字符，通配字符
mo21 = re.compile(r'.at')
words = mo21.findall('The cat in the hat sat on the flat mat')
print(words)
# 接收所有字符  .*
# 贪心模式匹配,.*将匹配最多的字符
mo22 = re.compile(r'names:(.*) phone number:(.*)')
users_info = mo22.findall('names:Mike phone number:15600000000 '
                          'names:Jack phone number:18100000000 '
                          'names:John phone number:16200000000 ')
print(users_info)
# 非贪心模式匹配,.*? 将匹配最少的字符
mo23 = re.compile(r'names:(.*?) phone number:(.*?) ')
users_info = mo23.findall('names:Mike phone number:15600000000 '
                          'names:Jack phone number:18100000000 '
                          'names:John phone number:16200000000 ')
print(users_info)

# 句点匹配换行符
mo24 = re.compile('.*')
sentences = mo24.search('I can see empty streets.\nBut I can\'t sleep empty sheets\n')
print(sentences.group())

mo25 = re.compile('.*', re.DOTALL)
sentences = mo25.search('I can see empty streets.\nBut I can\'t sleep empty sheets\n')
print(repr(sentences.group()))
print(sentences.group())
