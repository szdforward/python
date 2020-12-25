# -*- coding: UTF-8 -*-

# 默认参数
#有默认值的参数后面不能再跟无默认值的参数
def printinfo(name,age=35):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return
#调用
#如果调换了参数的顺序，则必须把参数名都带上
printinfo( age=50, name="miki" )
printinfo( name="miki" )

# 可变参数类型
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print("Output is: ",arg1)
   print('可变参数类型是：',type(vartuple))
   for var in vartuple:
      print(var)
   return
# 调用
printinfo( 10 )
printinfo( 70, 60, 50 )
# 结果:
# Output is:  10
# 可变参数类型是： <class 'tuple'>
# Output is:  70
# 可变参数类型是： <class 'tuple'>
# 60
# 50