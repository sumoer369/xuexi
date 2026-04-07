#输出Hello world
# print("Hello World")
# print("--------------")
# #字面量与变量
# print(300)#int
# print(2.11)#float
# print(True)#bool类型  ture=1 false=0
# print(True+1)
# print(False+1)
# print("Hello World")#str
# print(None)
# name="tfx"
# age=20
# print(name)
# print(age)
# age = 21
# print(age)
# num = 1
# num1 = 2
# print("两个变量和",num +num1)
# num,num1 = 1,2.3
# print(num,num1,num+num1)
#变量交换
# a = 1
# b = 2
# print("交换前",a,b)
# a, b = b, a
# print(a,b)
# c = a
# a = b
# b = c
# print("交换后",a,b)
# a=1
# b=2
# c=3
# print(a,b,c)
# e,f,g=a,b,c
# a=g
# b=e
# c=f
# print(a,b,c)
# print(type(100))
#isinstance()可以检查是否为指定数据类型
# print(isinstance(100.1,int))
# print(isinstance(100.1,float))
# s="""
# dadwada
# dawdaw
# dawda
#
# """
# print(s)
# s='wad'
# a="dadwa"
# print(a,s)
# aa='I\'m a boy'#单引号
# print(aa)
# print("inini\tinini\nininfiaf")#\t增加一个制表符的距离 \n换行
# a="ingig" "fbgubg"
# print(a)
# b="ingig"+"fbgubg"
# print(b)
# print(a+","+b)
# age = 10
# name = "ttt"
# # print(str(age) + "," + name)
# a=123
# b=111
# print("0000%s0000"%a)
# print("0000%s0000%s"%(b,a))
# print(f"dadad{a,b}")
# print(f"dadad{a}")
# print(f"dadad{b}{a}")
# a=input()
# print(f"{a}")
# a = input()
# b = input()
# print(f"{a}{b}")
#银行取钱  总额10000 输入密码后取100 显示剩余总额
# a=10000
# print("请输入您的密码")
# c=input()
# print(f"您剩余{a}元")
# b= input("请输入您要取的金额")
# print("剩余",a-int(b))
#计算机
# a=input("第一个数字")
# b=input("第二个数字")
# print(f"和为{int(a)+int(b)}")
# print(100//3)#整除
# print(10%3)#取余
# print(10**3)#指数
#优先级**--* / // %---+ -
#print(1+10/2*3**2)  #3**2=9 10/2=5 5*9=45 45+1=46
#要求输入两个数xy 分别计算x+y x-y
# x= input("x=")
# y= input("y=")
# print(f"x+y={int(x)+int(y)}")
# print(f"x-y={int(x)-int(y)}")
#小数可能会缺失
# x= float(input("x="))
# y= float(input("y="))
# print(f"x+y={x+y}")
# print(f"x-y={x-y}")#0.5-0.4=0.09999...8
# a += 1#a=a+1
# a/=1#a=a/1
# a//1#a=a//1
# a**=1#a=a**1
# == 等于  ！= 不等于
# print(1==2)#返回类型为bool
# a=int(input("输入一个数"))
# print(f"这个数是偶数{a%2 == 0}")#判断是不是偶数
# and #并且
# or # 或者
# not #取反
# print(1==1 and 1==0)
# print(1==1 and 2==2)
# print(1==1 or 1==0)
# print(1==0 or 1==2)
#输入一个数 判断范围在不在10-20之间
# a=int(input("输入一个数"))
# print(f"这个数在10-20之间{10<=a<=20}")
# print(f"这个数在10-20之间{10<=a and a<=20}")
# print(f"这个数在10-20之外{a<10 or a>20}")
a = int(input())
if a >= 60:
    print("你过关")
else:
    print("你完蛋")