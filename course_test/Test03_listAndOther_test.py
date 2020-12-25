#coding=utf-8

# 列表、元组、字段、set的用法

"""
列表
"""
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# print(list)          # Prints complete list ['abcd', 786, 2.23, 'john', 70.2]
# print(list[0])       # Prints first element of the list
# print(list[1:3])      # 含首不含尾 [786, 2.23]
# print("list[2:7]:", list[2:7])   #超出范围不报错 list[2:7]: [2.23, 'john', 70.2]
# print(list[2:])        # Prints elements starting from 3rd element [2.23, 'john', 70.2]
# print("list[:-3]:", list[:-3]) # 去除后几位元素，-3即为去除最后3个元素 list[:-3]: ['abcd', 786]
# print("list[:]:", list[:]) # 同list  list[:]: ['abcd', 786, 2.23, 'john', 70.2]
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
#更新list中的元素
# list[0]="python"
# print(list) #['python', 786, 2.23, 'john', 70.2]
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
#删除列表中的元素
# del list[0]
# print("list[:]:", list[:]) # list[:]: [786, 2.23, 'john', 70.2]
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
#列表对+和*的操作符与字符串相似。+号用于组合列表，*号用于重复列表
# print(list + tinylist)    # Prints concatenated lists ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
# print(tinylist * 2)    # Prints list two times [123, 'john', 123, 'john']
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# print(2.23 in list) #判定此元素是否在列表中，是的话为true，不是的话为false       True
# print(list.__sizeof__())   # 返回内存中列表的大小，以字节为单位。 80
# print(len(list)) # 返回列表的长度 5
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# list.append(['yyyy','zzzz']) #append是添加新的元素
# print(list) #['python', 786, 2.23, 'john', 70.2, ['yyyy', 'zzzz']]
# list.extend(['angelababy',66666]) #extend是在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# print(list) #['python', 786, 2.23, 'john', 70.2, ['yyyy', 'zzzz'], 'angelababy', 66666]
list = [ 'abcd', 786 , 2.23, 'john', 70.2 , 70.2]
# print(list.count(70.2)) #统计某个元素在列表中出现的次数 2
# print(list.index(70.2)) #从列表中找出某个值第一个匹配项的索引位置，索引从0开始 如果不在这个list中的话会报错  4
# list.insert(3, "insertobj") #将对象插入列表的对应下标的位置，如果这个下标已经超过最大下标，则放在最后
# print(list) #  ['abcd', 786, 2.23, 'insertobj', 'john', 70.2, 70.2]
# list.insert(-2, "obj") #将对象插入列表的对应下标的位置，如果这个下标为负数，则放在最后这几个数的元素前面
# print(list) # ['abcd', 786, 2.23, 'insertobj', 'john', 'obj', 70.2, 70.2]
# list.pop() #移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
# print(list) # ['abcd', 786, 2.23, 'insertobj', 'john', 'obj', 70.2]
# list.remove(786) #移除列表中某个值的第一个匹配项 如果不存在的话 会报错
# print(list) # ['abcd', 2.23, 'insertobj', 'john', 'obj', 70.2]
# list.reverse() #反转列表中元素，倒转
# print(list) # [70.2, 'obj', 'john', 'insertobj', 2.23, 'abcd']
# #list.sort() #对原列表进行排序 注意必须是同种类型的，否则会报错
# print(list)

##列表解析，用于生成列表
# ra = range(1,4)
# print(ra,type(ra)) # range(1, 4) <class 'range'>
# newlist=[2*i for i in (1,2,3)]
# print(newlist) # [2, 4, 6]
# newlist2=[2*i for i in range(1,5)] # range为包前不包后
# print(newlist2) # [2, 4, 6, 8]

# list1=['x','y','z']
# list2=[1,23]
# list3=[(i,j) for i in list1 for j in list2]
# print(list3) # [('x', 1), ('x', 23), ('y', 1), ('y', 23), ('z', 1), ('z', 23)]


"""
元组
"""
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')
#
# print(tuple)           # Prints complete list
# print(tuple[0])        # Prints first element of the list abcd
# print(tuple[1:3])      # Prints elements starting from 2nd till 3rd (786, 2.23)
# print(tuple[2:])       # Prints elements starting from 3rd element (2.23, 'john', 70.2)
# print(tinytuple * 2)   # Prints list two times (123, 'john', 123, 'john')
# print(tuple + tinytuple) # Prints concatenated lists ('abcd', 786, 2.23, 'john', 70.2, 123, 'john')
# tuple[1]=66666    #会报错，因为元组是不可变列表
# print(tuple)
#元组有一些函数可以使用，len指的是元组的元素个数，max min分别求元组的最大最小元素，但是需要注意的是，只有当元组中的类型一致时才可以使用max min，否则会报错
#元组中的元素值是不允许删除的，可以使用del语句来删除整个元组，例如:
# del tuple

"""
字典（哈希表类型 可以认为是map 由“键-值”对组成） #字典是无序的对象集合。字典由键和对应的值组成。字典也被称作关联数组或哈希表
"""
dict = {}
#也可如此创建字典：
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

#访问字典，修改元素
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

#字典内置函数&方法
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

