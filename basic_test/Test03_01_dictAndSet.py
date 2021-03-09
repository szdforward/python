# coding=utf-8

# 字典、set的用法


"""
字典（哈希表类型 可以认为是map 由“键-值”对组成） #字典是无序的对象集合。字典由键和对应的值组成。字典也被称作关联数组或哈希表
"""
dict = {}
# 貌似可以把字典看为一个对象，例如可以看下https://www.runoob.com/python3/python3-att-list-copy.html里面的笔记
# 也可如此创建字典：
# dict2 = { 'abc': 123, 98.6: 37 }
# dict['one'] = "This is one"
# dict[2]     = "This is two"
# print(dict['one'])       # Prints value for 'one' key    This is one
# print(dict[2])           # Prints value for 2 key    This is two
# del dict['one']  # 删除键是'name'的条目 如果键没有的话会报错
# print(dict) # {2: 'This is two'}
# dict.clear()   # 清空词典所有条目
# print(dict) # {}
# del dict    # 删除词典
# print(dict) # <class 'dict'>

# 访问字典，修改元素
# dict3= {'abc':1,"cc":[1,2,3]}
# dict3["cc"].append([5,6])
# dict3["cc"].extend([7,8])
# print(dict3["cc"]) # [1, 2, 3, [5, 6], 7, 8]
# dict3["dd"]=888
# print(dict3) # {'abc': 1, 'cc': [1, 2, 3, [5, 6], 7, 8], 'dd': 888}

# tinydict={"name":"john","code":6734,"dept":"sales"}
# tinydict['mygirl']="angelababy"
# print(type(tinydict.keys()),tinydict.keys())   # Prints all the keys  <class 'dict_keys'> dict_keys(['name', 'code', 'dept', 'mygirl'])
# print(tinydict.values()) # Prints all the values  dict_values(['john', 6734, 'sales', 'angelababy'])

# 字典内置函数&方法
# dict1={'a':1,'b':2}
# dict2={'a':1,'b':2,'c':3}
# print(len(dict1)) #计算字典元素个数，即键的总数。 2
# print(str(dict1)) #输出字典可打印的字符串表示。 {'a': 1, 'b': 2}
# print(type(dict1)) #返回输入的变量类型，如果变量是字典就返回字典类型。 <class 'dict'>
# dict0 = dict1.copy()   #返回一个字典的浅复制
# print(dict0,id(dict0),id(dict1)) # {'a': 1, 'b': 2} 37942016 37883136
# dict3 = dict.fromkeys(("a","b","c"))   #创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# print(dict3) # {'a': None, 'b': None, 'c': None}
# print(dict1.get('a', None))  #返回指定键的值，如果值不在字典中返回default值  1
# print(dict1.get('d', 0))  #返回指定键的值，如果值不在字典中返回default值  0
# entry = dict1.items()   #以列表返回可遍历的(键, 值) 元组列表
# print(type(entry)) # <class 'dict_items'>
# for ent in entry:
#    print(ent,ent[0],ent[1])
# # ('a', 1) a 1
# # ('b', 2) b 2
# dict1.setdefault('f',None)   #和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
# print(dict1) # {'a': 1, 'b': 2, 'f': None}
# dict1.update(dict2)  #把字典dict2的键/值对更新到dict里
# print(dict1) # {'a': 1, 'b': 2, 'f': None, 'c': 3}


# set 类型
# myset = {1,2}
# print(type(myset))  # <type 'set'>
# myset.add(2)
# print(myset) #set存储的是不相同的元素，即使上面添加了两个2，结果也只有一个2  {1, 2}
