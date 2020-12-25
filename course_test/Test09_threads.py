#coding=utf-8
# Python中的多线程是伪线程；不能充分利用cpu中的多核，但是在io等待型的场景下多线程还是可以提高效率
# Python中的多线程有多种实现方式，利用threading包实现是比较普遍的做法
import threading
from time import ctime,sleep
def music(func):
    for i in range(2):
        print("i was listening to %s. %s" %(func,ctime()))
        sleep(1)

def movie(func):
    for i in range(2):
        print("i was at the %s! %s" %(func,ctime()))
        sleep(5)

threads=[]
t1=threading.Thread(target=music,args=('爱情买卖',))
threads.append(t1)
t2=threading.Thread(target=movie,args=('阿凡达',))
threads.append(t2)
# if __name__  ==  '__main__' :
for t in threads:
    # t.setDaemon(True) #设置为守护进程  如果不设置为守护进程的话，最后的print语句不会打印出来
    t.start()
# t.join()
print("all over %s" %ctime())