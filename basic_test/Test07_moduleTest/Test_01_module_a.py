#coding=utf-8
"""
这是模块注释  相当于会把这里的信息赋予给 __doc__ 变量
"""
def print_func( par ):
   print("Hello : ", par)
   return


def sum_func(x,y):
   print("sum : ", x+y)
   return

"""
当该脚本直接被解释执行时，其内置变量__name__的值会被python执行器赋值“__main__”
而如果该脚本是被别的脚本作为模块导入时，__name__的值就不会等于“__main__”,szd-而是等于此模块的名字
所以，如果不想让别的脚本导入本模块时执行的代码，就可以用如下方式处理：
"""
if __name__ == '__main__':
    print("in module_a   aaaaaaa")
print('in module a: ', __name__)
print(__doc__) # 这是模块注释  相当于会把这里的信息赋予给 __doc__ 变量
class A:
    def x(self):
        print('haha')
print(A.__module__) # __main__
print(A.__name__) # A