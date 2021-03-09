# coding=utf-8
#python的函数调用是 引用传递

# 定义函数的基本形式
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4])
   print("Values inside the function: ", mylist)
   return

# 调用函数
mylist = [10,20,30]
changeme( mylist ) # Values inside the function:  [10, 20, 30, [1, 2, 3, 4]]
print("Values outside the function: ", mylist) # Values outside the function:  [10, 20, 30, [1, 2, 3, 4]]

# 计算累计和
def func1(i):
    if i < 100:
        return i + func1(i + 1)
    return i

print(func1(99))
