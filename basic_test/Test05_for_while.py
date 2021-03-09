#coding=utf-8
# 求出大于等于10小于20的质数(素数)
# for num in range(10,20):   #to iterate between 10 to 20
#     flag = True
#     for i in range(2,num):   #to iterate on the factors of the number
#         if num%i == 0:       #to determine the first factor
#             j=num/i           #to calculate the second factor
#             print('%d equals %d * %d' % (num,i,j),"不是质数")
#             flag = False
#             break            #跳出本层循环
#     if flag:
#         print(num, '是质数')

#=========步长================
# 可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
# for i in range(10,30,3):
#     print(i)

# while循环使用else语句  在 while … else 在条件语句为 false 时执行 else 的语句块
# count = 0
# while(count < 5):
#    print(count, " is  less than 5")
#    count = count + 1
# else:
#    print(count, " is not less than 5")

# break和continue的使用
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。 加上break的话。while后面的else也不会执行了
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

# pass 语句 是空语句，是为了保证程序结构的完整性 不做任何事情，一般用做占位语句

# =============================遍历一个序列（带索引）
# 您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i,a[i])
# # 或者使用内置 enumerate 函数进行遍历
# print("enumerate")
# for i,j in enumerate(a):
#     print(i,j)

# ======================1到100的和
# print(sum(range(101)))