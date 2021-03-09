#coding=utf-8
# 导入模块时，是按照sys.path变量的值搜索模块，sys.path的值是包含每一个独立路径的列表，包含当前目录、python安装目录、PYTHONPATH环境变量，
# 搜索顺序按照路径在列表中的顺序（一般当前目录优先级最高）
# 并且注意第一次导入模块的时候，会默认把该模块下的命令都执行一遍 模块只会导入一次

# import Test_01_module_a
# Test_01_module_a.print_func("haha") #Hello :  haha


# from Test_01_module_a import  *
# print_func("heihei") #Hello :  heihei


from Test_01_module_a import print_func as pf
pf("xixi") #Hello :  xixi

print('in module b,' ,__name__) # in module b, __main__
