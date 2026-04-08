# print("hello world")
# my_name = "tfx"
# age = 20
# zhuanye = "计算机科学与技术"
# print(my_name,age,zhuanye)
# fenshu = int(input())
# if fenshu >= 60:
#     print("你过关")
# else:
#     print("你完蛋")
#----------------------复习----------------------------
# zhanghao = int(input("创建您的账号"))
# mima = int(input("创建密码"))
# print(f"您的账号密码为{zhanghao} ,{mima}")
# print("请输入账号密码进行登录")
# shuru_zhanghao = int(input("账号："))
# shuru_mima = int(input("密码："))
# if shuru_zhanghao == zhanghao and shuru_mima==mima:
#     print("登录成功")
# else:
#     print("您的账号或密码错误")
# year = int(input("请输入一个年份"))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}不是闰年")
# shuzi= int(input("输入一个数字判断奇数偶数"))
# if shuzi%2==0:
#     print("偶数")
# else:
#     print("奇数")
# age=int(input("输出您的年龄"))
# if age>=18:
#     print("您已成年")
# else:
#     print("您未成年")
# num=int(input("输入一个非0数字判断正负"))
# if num>0:
#     print("正数")
# else:
#     print("负数")
# num=int(input("输入一个数字判断正负或0:"))
# if num>0:
#     print("正数")
# elif num==0:
#     print("0")
# else:
#     print("负数")
# chengji = int(input("输入考试成绩"))
# if chengji < 60:
#     print("不及格")
# elif chengji > 60 and chengji < 80:
#     print("及格")
# elif chengji > 80 and chengji < 100:
#     print("优秀")
# else:
#     print("吹牛逼呢")
# print("输入三角形的三条边长")
# a,b,c=int(input()),int(input()),int(input())
# if a+b>c and a+c>b and b+c>a:
#     print("普通三角形")
# elif a==b==c:
#     print("等边三角")
# elif a==b or b==c or c==a:
#     print("等腰三角形")
# else:
#     print("无法组成三角形")
# print("输入三角形的三条边长")
# a,b,c=int(input()),int(input()),int(input())
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print("等边三角")
#     elif a==b or a==c or b==c:
#         print("等腰三角")
#     else:
#         print("普通三角形")
# else:
#     print("无法组成三角形")
# yongdian = float(input("您的用电量 度："))
# if yongdian < 2880:
#     print(f"您要交{yongdian*0.4883}元")
# elif yongdian >= 2880 and yongdian <= 4800:
#     print(f"您要交{yongdian*0.5383}元")
# else:
#     print(f"您要交{yongdian*0.7883}元")
# day = int (input("输入今天周几（1-7）"))
# match day:
#     case 1:print("周一")
#     case 2:print("周二")
#     case 3:print("周三")
#     case 4:print("周四")
#     case 5:print("周五")
#     case 6|7:print("周末")
#     case _:print("错误")
# num1,yunsuan,num2= float (input("输入第一个数")), input("输入运算符"),float (input("输入第二个数"))
# match yunsuan:
#     case "+":print(f"{num1} + {num2}={num1+num2}")
#     case "-":print(f"{num1} - {num2}={num1-num2}")
#     case "*":print(f"{num1} * {num2}={num1*num2}")
#     case "/":
#         if num2!=0:
#             print(f"{num1} / {num2}={num1/num2}")
#         else:
#             print("除数不能为0")
#     case _:print("出错")
# num1,yunsuan,num2= float (input("输入第一个数")), input("输入运算符"),float (input("输入第二个数"))
# match yunsuan:
#     case "+":print(f"{num1} + {num2}={num1+num2}")
#     case "-":print(f"{num1} - {num2}={num1-num2}")
#     case "*":print(f"{num1} * {num2}={num1*num2}")
#     case "/"if num2!=0:
#                 print(f"{num1} / {num2}={num1/num2}")
#     case _:print("出错")
# i=0
# while i<10:
#     i=i+1
#     print(f"kkt*{i}")
# i,j=1,0
# while i <= 100:
#     if i%2==0:
#         j += i
#     i+=1
# print(j)
# mag= "hello world"
# for i in mag:
#     print(i)
# print("结束")
# j = 0
# for i in range(1,101,2):
#     j += i
# print(j)
# j = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         j += i
# print(j)
# kuan = int(input())
# chang = int(input())
# for i in range(kuan):
#     for j in range(chang):
#         print("*",end=" ")
#     print()
#99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end=" ")
#     print()
# a = "▮"
# b = "▯"
# for j in range(0,9):
#     for i in range(0,9):
#         if (i+j) % 2 == 0:
#             print(a,end=" ")
#         else:
#             print(b,end=" ")
#     print()
# zhanghao=int(input("创建账号"))
# mima=int(input("创建密码"))
# print(f"账号：{zhanghao}密码：{mima}")
# print("请登录:")
# zhanghao1 = int(input("账号:"))
# mima1 = int(input("密码:"))
# while zhanghao1!=zhanghao or mima1!=mima:
#    print("账号或密码错误")
#    zhanghao1 = int(input("账号:"))
#    mima1 = int(input("密码:"))
# else:
#     print("登录成功")
# ok_zhanghao1,ok_zhanghao2,ok_mima1,ok_mima2=123456,111,123456,111
# while True:
#     zhanghao=input("账号")
#     mima=input("密码")
#     if zhanghao=="" or mima=="":
#         print("账号或密码不能为空")
#         continue
#     elif ok_zhanghao1==zhanghao and ok_mima1==mima:
#         print("登录成功")
#         break
#     elif ok_zhanghao2==zhanghao and ok_mima2==mima:
#         print("登录成功")
#         break
#     else:
#         print("账号或密码错误")
# ok_zhanghao1,ok_zhanghao2,ok_mima1,ok_mima2=123456,111,123456,111
# for i in range(5):
#     zhanghao=input("账号")
#     mima=input("密码")
#     if zhanghao=="" or mima=="":
#         print("账号或密码不能为空")
#         continue
#     elif ok_zhanghao1==zhanghao and ok_mima1==mima:
#         print("登录成功")
#         break
#     elif ok_zhanghao2==zhanghao and ok_mima2==mima:
#         print("登录成功")
#         break
#     else:
#         print("账号或密码错误")
# print("已锁定")
# import random
# ok_num = random.randint(1,100)
# while True:
#    num = int(input("一个1到100之内的数字："))
#    if ok_num == num:
#        break
#    elif num > ok_num:
#        print("大了")
#        continue
#    else:print("小了")
# print("猜对了")



