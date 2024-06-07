from lxml import etree

# 解析本地文件etree.parse
# 解析服务器数据etree.HTML

tree = etree.parse('XX.html')

#路径查询
# li_list = tree.xpath('//body//li')

#谓词查询 查找所有id为li的标签
# li_list = tree.xpath('//ul/li[@id]/text()')

#找到id为l1的标签  注意引号的问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

#找到id为l1的li标签的class的属性值
# li_list = tree.xpath('//ul/li[@id="l1"]/@class')


#模糊查询 查询id带有l的li标签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# id以c开头
# li_list = tree.xpath('//ul/li[starts-with(@id,"l"]/text()')

# 逻辑运算 查询id为l1和c1的
# li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
# 查询id为l1或者l2的
li_list = tree.xpath('//ul/li[@id="l1" or @id="l7"]/text()')


print(li_list)
print(len(li_list))
