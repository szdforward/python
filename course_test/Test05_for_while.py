#coding=utf-8
# 求出大于等于10小于20的质数
for num in range(10,20):   #to iterate between 10 to 20
    for i in range(2,num):   #to iterate on the factors of the number
        if num%i == 0:       #to determine the first factor
            j=num/i           #to calculate the second factor
            print('%d equals %d * %d' % (num,i,j))
            break            #跳出本层循环
        else:                   # else part of the loop
            print(num, 'is a prime number')

# while  test
count = 0
while(count < 5):
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")
