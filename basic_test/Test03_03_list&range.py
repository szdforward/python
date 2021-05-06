# coding=utf-8

# 列表的用法

"""
列表
"""
import copy

mylist = ['abcd', 786, 2.23, 'john', 70.2]
# print(mylist)          # Prints complete mylist ['abcd', 786, 2.23, 'john', 70.2]
# print(mylist[0])       # Prints first element of the mylist
# print(mylist[1:3])      # 含首不含尾 [786, 2.23]
# print("mylist[2:7]:", mylist[2:7])   #超出范围不报错 mylist[2:7]: [2.23, 'john', 70.2]
# print(mylist[2:])        # Prints elements starting from 3rd element [2.23, 'john', 70.2]
# print("mylist[:-3]:", mylist[:-3]) # 去除后几位元素，-3即为去除最后3个元素 mylist[:-3]: ['abcd', 786] 也可以理解为从开头到-3的元素（含头不含尾。即不含-3元素）
# print("mylist[:]:", mylist[:]) # 同mylist  mylist[:]: ['abcd', 786, 2.23, 'john', 70.2]
# 按照步长截取
# print(mylist[::2]) # ['abcd', 2.23, 70.2]  表示从头到尾 步长为2 从第一个开始，跨1步为786，跨2步为2.23 默认步长为1
# a='python'
# b=a[::-1]
# print(b) #nohtyp
# c=a[::-2]
# print(c) #nhy
mylist = ['abcd', 786, 2.23, 'john', 70.2]
# 更新mylist中的元素
# mylist[0]="python"
# print(mylist) #['python', 786, 2.23, 'john', 70.2]
mylist = ['abcd', 786, 2.23, 'john', 70.2]
# 删除列表中的元素
# del mylist[0]
# print("mylist[:]:", mylist[:]) # mylist[:]: [786, 2.23, 'john', 70.2]
mylist = ['abcd', 786, 2.23, 'john', 70.2]
tinymylist = [123, 'john']
# 列表对+和*的操作符与字符串相似。+号用于组合列表，*号用于重复列表
# print(mylist + tinymylist)    # Prints concatenated mylists ['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
# print(tinymylist * 2)    # Prints mylist two times [123, 'john', 123, 'john']
mylist = ['abcd', 786, 2.23, 'john', 70.2]
# print(2.23 in mylist) #判定此元素是否在列表中，是的话为true，不是的话为false       True
# print(mylist.__sizeof__())   # 返回内存中列表的大小，以字节为单位。 80
# print(len(mylist)) # 返回列表的长度 5 列表元素个数
mylist = ['abcd', 786, 2.23, 'john', 70.2]
# mylist.append(['yyyy','zzzz']) #append是添加新的元素  注意append是浅拷贝 如果append一个对象时，需要特别注意：
# num = [2]
# mylist.append(num)
# print(mylist)  # ['abcd', 786, 2.23, 'john', 70.2, [2]]
# num[0] = 34
# print(mylist)  # ['abcd', 786, 2.23, 'john', 70.2, [34]]
# 如果希望深度拷贝的话：可以这样：mylist.append(copy.deepcopy(num))
# 复制一个新的list的话，不影响旧的list：所以一般情况下想复制得到一个新列表并改变新列表内元素而不影响原列表，可以采用这种赋值方式：
# a = [1, 2, 3]
# d = a[:]
# 或者使用copy模块里 copy()函数也是可以的，另外使用list自带的copy()方法也是可以的，相当于开辟了新的内存空间存储新列表


# print(mylist) #['python', 786, 2.23, 'john', 70.2, ['yyyy', 'zzzz']]
# mylist.extend(['angelababy',66666]) #extend是在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)
# print(mylist) #['python', 786, 2.23, 'john', 70.2, ['yyyy', 'zzzz'], 'angelababy', 66666]
mylist = ['abcd', 786, 2.23, 'john', 70.2, 70.2]
# print(mylist.count(70.2)) #统计某个元素在列表中出现的次数 2
# print(mylist.index(70.2)) #4  从列表中找出某个值第一个匹配项的索引位置，索引从0开始 如果不在这个mylist中的话会报错  index还可以接参数，表名从哪个位置开始查找
# print(mylist.index(70.2,-1))#5  表示从最后一个查找
# mylist.insert(3, "insertobj") #将对象插入列表的对应下标的位置，如果这个下标已经超过最大下标，则放在最后
# print(mylist) #  ['abcd', 786, 2.23, 'insertobj', 'john', 70.2, 70.2]
# mylist.insert(-2, "obj") #将对象插入列表的对应下标的位置，如果这个下标为负数，则放在最后这几个数的元素前面
# print(mylist) # ['abcd', 786, 2.23, 'insertobj', 'john', 'obj', 70.2, 70.2]
# mylist.pop() #移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
# print(mylist) # ['abcd', 786, 2.23, 'insertobj', 'john', 'obj', 70.2]

#=============remove元素
# mylist.remove(78622) #移除列表中某个值的第一个匹配项 如果不存在的话 会报错  ValueError: mylist.remove(x): x not in mylist
# print(mylist) # ['abcd', 2.23, 'insertobj', 'john', 'obj', 70.2]
# 如果需要大批量删除的话，可以看下这个：https://www.runoob.com/python3/python3-att-mylist-remove.html
# print(set(mylist)-set([786,2.23]))#{'abcd', 'john', 70.2}
# 另外使用set来做两个mylist的比较，方法会比较快。例如取交集，取差集等
# a=[1,2,3]
# b=[2,3,4]
# diff=list(set(a).difference(set(b)))#代表在a里面，不在b里面
# print(diff) # [1]

# mylist.reverse() #反转列表中元素，倒转
# print(mylist) # [70.2, 'obj', 'john', 'insertobj', 2.23, 'abcd']

#===============sort排序  list.sort() 函数在排序时，使用的是小于号对比
# mylist2=[23,56,3,12,33,45,21,9]
# mylist2.sort() #对原列表进行排序 注意必须是同种类型的，否则会报错  sort的话，还可以选择升序还是降序
# print(mylist2)#[3, 9, 12, 21, 23, 33, 45, 56]
# 以下实例演示了通过指定列表中的元素排序来输出列表：具体的类的排序（自定义排序的属性），还可以看这个：https://www.runoob.com/python3/python3-att-list-sort.html
# 另外教程中还有 根据列表中元素的多个属性进行排序、动态的根据用户指定的索引进行排序
# randomList = [(2, 2), (3, 4), (4, 1,5), (1, 3,44,6)]
# def takeSecond(elem):
#     return elem[1]
# randomList.sort()
# print(randomList)#[(1, 3), (2, 2), (3, 4), (4, 1)]
# randomList.sort(key=takeSecond)
# print(randomList)#[(4, 1), (2, 2), (1, 3), (3, 4)]
# randomList.sort(key=lambda ele: len(ele))#这种跟上面的takeSecond是类似的，只不过是简写了 默认是按升序排序
# print(randomList)#[(2, 2), (3, 4), (4, 1, 5), (1, 3, 44, 6)]
# randomList.sort(key=lambda ele: len(ele),reverse=True)#这种跟上面的takeSecond是类似的，只不过是简写了 默认是按升序排序
# print(randomList)#[(1, 3, 44, 6), (4, 1, 5), (2, 2), (3, 4)]

# print(ord("一"))#获取的是字符的Unicode编码
# print(chr(ord("一")))#chr 是把unicode编码值转换为对应的字符

##列表解析，用于生成列表 列表推导式的使用
# ra = range(1,4)
# print(ra,type(ra)) # range(1, 4) <class 'range'>
# newmylist=[2*i for i in (1,2,3)]
# print(newmylist) # [2, 4, 6]
# newmylist2=[2*i for i in range(1,5)] # range为包前不包后
# print(newmylist2) # [2, 4, 6, 8]
li = [1,2,3,4,5,6,7,8,9]
# print (dict([(x,x*10) for x in li]))#{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}
# print ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])#[(5, 9), (7, 9), (9, 9)]
# 可以理解为拉链操作：
# vec=[2,4,6]
# vec2=[4,3,-9]
# sq = [(vec[i],vec2[i]) for i in range(len(vec))]
# print (sq)#[(2, 4), (4, 3), (6, -9)]
# mylist1=['x','y','z']
# mylist2=[1,23]
# mylist3=[(i,j) for i in mylist1 for j in mylist2]
# print(mylist3) # [('x', 1), ('x', 23), ('y', 1), ('y', 23), ('z', 1), ('z', 23)]

#生成二维列表
list_2d = [ [0 for i in range(5)] for i in range(5)]
list_2d[0].append(3)
list_2d[0].append(5)
list_2d[2].append(7)
# print(list_2d)#[[0, 0, 0, 0, 0, 3, 5], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 7], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# 创建空列表
list_empty = [0]*10
list_empty = [None]*10

# 倒序遍历 range的用法 range可以很方便的给我们生成自然数序列
for i in range(10,-5,-1):
    print(i,end="%")#10%9%8%7%6%5%4%3%2%1%0%-1%-2%-3%-4%
for i in range(10,0,-1):#szd-感觉最后的这个数 步长 其实就可以理解为减1，-2的话就代表减2  默认是1即加1
    print(i,end=",")#10,9,8,7,6,5,4,3,2,1,


# 使用list[0]=xxx 时需要注意的事项：如果list是一个空的，没有一个元素，进行list[0]就会出现错误：
# list assignment index out of range：列表超过限制
# 解决办法为：应该使用iplist.insert(i, ip) 或者iplist.append()