#coding=utf-8
"""
元组 tuple与list类似，不同之处在于tuple的元素不能修改 元组的元素不可变，但可以包含可变对象如list等  如果想新增的话，可以用两个元组相加 也不能删除元素
"""
# 注意定义一个元素的元组，必须加逗号

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
# del tuple #这样的话，就把当前的对象删除了

# 元组的不可变指的是元组指向的内存中的内容不可变 其实可以把当前的元组重新赋一个的 例如：
tuple1 = (1,2)
tuple1 = (2,)
# print(tuple1)#(2,)

#通过间接的方法修改元组
# tuple2=(1,2,4,5)
# tuple2=tuple2[:2]+(3,)+tuple2[2:]
# print(tuple2) #(1, 2, 3, 4, 5)

# 具名元组 可以为元组内部的元素命令，感觉相当于一个类了
from collections import namedtuple
# 两种方法来给 namedtuple 定义方法名
# namedtuple("User","name age id")
User = namedtuple("User",["name","age","id"])
# 赋值
# user1 = User("lisi","13","119")
user = User(name="lisi",age=13,id="120")
# print(user)#User(name='lisi', age=13, id='120')
# 打印所有的属性
# print(user._fields)#('name', 'age', 'id')
#使用_make创建实例
user2=User._make(["rubbo",23,"330"])
# print(user2)#User(name='rubbo', age=23, id='330')
# 修改对象的属性  应用了下，不起作用...szd
# user2._replace(name="dddd")
# print(user2)
# 将User对象转换为字典，使用_asdict
# print(user2._asdict())#{'name': 'rubbo', 'age': 23, 'id': '330'}


