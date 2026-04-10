# s=[1,2,3,4,5,6,7,8,9]
# s.append(33)
# print(s)
# s.pop(5)
# print(s)
# s.insert(3,41)
# print(s)
# print(s[3])
# print(s[:5])
# print(s[:-2])
# s.sort()
# print(s)
# s.remove(3)
# print(s)
# s.reverse()
# print(s)
# import random
# liebiao=[]
# for i in range(10):
#     s=random.randint(1,100)
#     liebiao.append(s)
# liebiao.sort()
# print(liebiao)
# print(f"最小值{liebiao[0]}")
# print(f"最小值{min(liebiao)}")
# print(f"最大值{liebiao[-1]}")
# print(f"最大值{max(liebiao)}")
# print(f"平均值{sum(liebiao)/len(liebiao)}")
# liebiao1=[1,2,3,4,5,4,5,4,6,4,1]
# liebiao2=[6,6,3,4,8,2,11,1,0,1156]
# for i in liebiao1:
#     liebiao2.append(i)
# print(liebiao2)
# liebiao=[]
# for j in liebiao2:
#     if j in liebiao:
#         continue
#     else:
#         liebiao.append(j)
# print(liebiao)
#简化合并部分
# liebiao1=[1,2,3,4,5,4,5,4,6,4,1]
# liebiao2=[6,6,3,4,8,2,11,1,0,1156]
# s=liebiao1 + liebiao2
# liebiao = [*liebiao1,*liebiao2]
# print(liebiao)
# print(s)
# liebiao3=[]
# for i in liebiao:
#     if i in liebiao3:
#         continue
#     else:
#         liebiao3.append(i)
# print(liebiao3)
# liebiao = []
# for i in range(20):
#     liebiao.append(i**2)
# print(liebiao)
# import random
# s=[]
# s1=[]
# for i1 in range(10):
#     s.append(random.randint(1,30))
# print(s)
# for j in s:
#     if j%2==0:
#         s1.append(j**2)
# print(s1)
# liebiao=[i**2 for i in range(1,21)]
# print(liebiao)
# liebiao=[i**2 for i in range(1,21) if i%2==0]
# print(liebiao)
# list1 = ['a','b','c']
# list2 = ['A','B','C']
# list3 = ['w','s','a','d']
# list=list1+list2+list3
# print(list)
# list_1=[]
# for i in list:
#     if i not in list_1:
#         list_1.append(i)
# print(list_1)
# list_1.sort()
# print(list_1)
# s="hello world"
# print(type(s[3]))
# print(s[1:5])
# print(s[6:1:-1])
# print(s.find("e"))
# print(s.count("l"))
# print(s.upper())
# print(s)
# s.lower()
# print(s)
# print(s.split(' '))
# print(s.replace('l','o'))
# print(s.startswith('s'))
# print(s.startswith('h'))
# print(s.strip('d'))
# print(s.endswith("ld"))
from itertools import count

# email = input("邮箱:")
# if email.count("@") != 1 or "." not in email:
#     print("邮箱格式错误")
# else:
#     print("格式正确")
# zifu1=input("输入回文")
# if zifu1[::-1]==zifu1:
#     print("这是回文")
# s=[]
# zifu2=input("原字符")
# s = zifu2[::-1].upper()
# print(s)
# yuanzu=(1,2,3,4,5,6,7,5,9,10)
# print(yuanzu.count(5))
# print(yuanzu.index(5))
# print(yuanzu[-1])
# print(yuanzu[::-1])
# print(type(yuanzu))
# print(yuanzu)
# s=yuanzu[:6]
# print(s)
# s=(1)
# print(s)
# print(type(s))
# s=(1,)
# print(s)
# print(type(s))
# s=('ss',2,4,5,8,4)
# s1='d',2,4,'a',8,4
# a,b,c,*d=s1
# print(a,b,c,d)
# a,b,c,*d=s
# print(a,b,c,d)
# print(type(s1),type(a))
# a= 10
# b=20
# a,b=b,a# a,b = 相当于解包 = b,a相当于组包
# print(a,b) 