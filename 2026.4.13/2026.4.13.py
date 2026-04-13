# num = 100
# def are(r):
#     p = 0
#     global num
#     num += 1
#     print(num)
#     return p+1,2*3.14*r
# print(num)
# a=are(10)
# print(num)
# print(a)
# # print(p)
# def ss(a,b,c,d=0):
#     print(a,b,c,d)
#     return a,b,c,d
#
# print(ss(1,2,3,4))
# print(ss(b=2,c=3,a=4,d=5))
# print(ss(1,2,d=3,c=4))
# print(ss(b=2,c=3,a=4))
# def ss(*a,**a1):
#     max1=max(a)
#     min1=min(a)
#     avg=sum(a)/len(a)
#     print(a1.get("uuu"))
#     return max1,min1,round(avg,1)
# print(ss(1,2,3,4,5,6,5,4,3,9,10))
# a=ss(1,2,3,4,5,6,uuu=1,ada=2)
# print(a)
# def add(a, b):
#     return a+b
# def sub(a, b):
#     return a-b
# def mul(a, b,ss):
#     return ss(a,b)
# a=mul(10,20,sub)
# print(a)
# add=lambda x,y: x + y
# sub=lambda x,y: x - y
# print(add(3,4))
# print(sub(3,4))
# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# print(data_list)
# data_list.sort(key=lambda x: len(x))
# print(data_list)
# def jiecheng(a):
#     s = 1
#     for i in range(1,a+1):
#         s *= i
#     return s
# print(jiecheng(1))
# print(jiecheng(4))
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n-1)
# print(jc(5))
# def calc_order_cost(*args:tuple[str,int,int],youhui:int,jifen:int,yunfei:float):
#     total_price = [i[1]*i[2] for i in args]
#     total_cost = sum(total_price)
#     #优惠券
#     if total_cost >= 5000 and youhui <= total_cost:
#         total_cost -= youhui
#     #积分
#     if total_cost >= 5000 and jifen//100 <= total_cost:
#         total_cost -= jifen//100
#     #运费
#     return total_cost+yunfei
# a=calc_order_cost(("手机",1111,2),("相机",1999,3),youhui=11,jifen=200,yunfei=2.6)
# print(a)
# import random
# import random as r
# from random import randint as r
# from random import*
# for i in range(10):
#     print(r(1,10))
#     print(randint(2,10))
# from a413_1 import *
# # print(a413_1.NAME)
# # print(a413_1.area(5))
# # print(a413_1.PI)
# print(area(5))
# aa()
# import a3.aa1
# from a3 import*
# print(aa2.add(1,3))
# print(a3.aa1.sub(1, 3))
