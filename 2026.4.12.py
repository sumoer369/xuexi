# set1 = {"d","da","a","bb",0,5,0,5}
# print(type(set1))
# print(set1)
# s1={}
# print(type(s1))
# print(s1)
# s2=set()
# print(type(s2))
# print(s2)
# s2.add(0)
# s2.add(1)
# s2.add(2)
# print(s2)
# s2.remove(2)
# print(s2)
# e=s2.pop()
# print(e)
# s2.clear()
# print(s2)
# a1={1,2,3,4}
# a2={2,3,4,5,6}
# print(a1.difference(a2))
# print(a2.difference(a1))
# print(a1.union(a2))
# print(a1.intersection(a2))
#
# football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# basketball_set = {"张铁", "墨居仁", "王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# print(f"同时选修法语和艺术{french_set.intersection(art_set)}")
# s1=french_set&art_set
# print(s1)
# print(f"同时选了四个{basketball_set.intersection(french_set,football_set,art_set)}")
# all_set=football_set & basketball_set & art_set & french_set & art_set
# print(all_set)
# print(f"选了足球但是没有篮球{football_set.difference(basketball_set)}")
# s2 = football_set - basketball_set
# print(s2)
# s3 = {s for s in football_set if s not in basketball_set}
# print(s3)
# all = football_set | basketball_set | art_set | french_set
# print(all)
# all_list = [*football_set,*basketball_set,*art_set,*french_set]
# print(all_list)
# for s in all:
#     print(f"{s}选了{all_list.count(s)}")
# dict1 = {"王琳":605,"李明":555,"方源":705,"韩立":365,"李明":100}
# score=dict1["王琳"]
# print(score)
# score=dict1["李明"]
# print(score)
# dict1["王琳"]= 101
# print(dict1["王琳"])
# dict1["小米"]=256
# print(dict1)
# dict1.pop("韩立")
# print(dict1)
# del dict1["李明"]
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
# for k in dict1.keys():
#     print(k,dict1[k])
# print("-------")
# for k,v in dict1.items():
#     print(k,v)
# print("-------")
# for s in dict1.items():
#     print(s[0],s[1])
# gouwuche={"商品1":{"jiage":100,"shuliang":20},
#           "商品2":{"jiage":200,"shuliang":20},
#           "商品3":{"jiage":300,"shuliang":20},
#           "商品4":{"jiage":400,"shuliang":20},
#           }
# while 1:
#     print("欢迎使用购物车菜单系统")
#     print("-------------------")
#     print("#\t1.添加购物车\t#")
#     print("#\t2.修改购物车\t#")
#     print("#\t3.删除购物车\t#")
#     print("#\t4.查询购物车\t#")
#     print("#\t5.退出购物车\t#")
#     print("-------------------")
#     caozuo = input("请输入您的操作:")
#     match caozuo:
#         case '1':
#             new_name=input("请输入商品名称：")
#             new_jiage=int(input("请输入商品价格"))
#             new_shuliang=int(input("请输入商品数量"))
#             if new_name in gouwuche:
#                 print("商品已存在")
#             else:
#                 gouwuche[new_name]={"jiage":new_jiage,"shuliang":new_shuliang}
#                 print("添加成功")
#         case '2':
#             new_name = input("请输入要修改商品名称：")
#             if new_name not in gouwuche:
#                 print("商品不存在")
#                 continue
#             else:
#                 new_jiage = int(input("请输入最新商品价格"))
#                 new_shuliang = int(input("请输入最新商品数量"))
#                 gouwuche[new_name] = {"jiage": new_jiage, "shuliang": new_shuliang}
#                 print("修改成功")
#         case '3':
#             new_name = input("请输入要删除商品名称：")
#             if new_name not in gouwuche:
#                 print("商品不存在")
#             else:
#                 del gouwuche[new_name]
#                 print("删除成功")
#         case '4':
#             for i in gouwuche.keys():
#                 info=gouwuche[i]
#                 print(f"商品名称{i},商品价格{info["jiage"]},商品数量{info["shuliang"]}")
#         case '5':
#             break
#         case _:
#             print("操作错误")
# print("欢迎使用学生刺激管理系统")
# xitong={"王琳":{"yuwen":100,"shuxue":90,"yingyu":99},
#         "小米":{"yuwen":99,"shuxue":70,"yingyu":60}
#         }
# mm="""
# ##############################
# #      1.添加学生信息          #
# #      2.修改学生信息          #
# #      3.删除学生信息          #
# #      4.查询学生信息          #
# #      5.列出所有学生          #
# #      6.统计班级成绩          #
# #      7.退出系统             #
# ##############################
# """
# # all_yuwen=xitong["王琳"]
# # print(all_yuwen["yuwen"])
# while True:
#     print(mm)
#     caozuo = input("请输入您的操作")
#     match caozuo:
#         case "1":
#             name=input("请输入学生姓名")
#             if  name in xitong:
#                 print("已存在")
#                 continue
#             else:
#                 yuwen_new=int(input("请输入语文成绩"))
#                 shuxue_new=int(input("请输入数学成绩"))
#                 yingyu_new=int(input("请输入英语成绩"))
#                 xitong[name]={"yuwen":yuwen_new,"shuxue":shuxue_new,"yingyu":yingyu_new}
#         case "2":
#             name = input("请输入学生姓名")
#             if  name not in xitong:
#                 print("不存在")
#                 continue
#             else:
#                 yuwen_new = int(input("请输入语文成绩"))
#                 shuxue_new = int(input("请输入数学成绩"))
#                 yingyu_new = int(input("请输入英语成绩"))
#                 xitong[name] = {"yuwen": yuwen_new, "shuxue": shuxue_new, "yingyu": yingyu_new}
#
#         case "3":
#             name = input("请输入学生姓名")
#             if name not in xitong:
#                 print("不存在")
#                 continue
#             else:
#                 del xitong[name]
#         case "4":
#             name=input("请输入学生姓名")
#             if name not in xitong:
#                 print("学生不存在")
#                 continue
#             else:
#                 print(xitong[name])
#         case "5":
#             for i in xitong:
#                 info = xitong[i]
#                 print(f"{i},语文{info['yuwen']}，数学：{info["shuxue"]}，英语{info["yingyu"]}")
#                 continue
#         case "6":
#             all_yuwen= [a["yuwen"] for a in xitong.values()]
#             all_shuxue= [a["shuxue"] for a in xitong.values()]
#             all_yingyu = [a["yingyu"] for a in xitong.values()]
#             high_yuwen= max(all_yuwen)
#             high_shuxue= max(all_shuxue)
#             high_yingyu= max(all_yingyu)
#             low_yuwen= min(all_yuwen)
#             low_shuxue= min(all_shuxue)
#             low_yingyu= min(all_yingyu)
#
#             name_high_yuwen=[s for s,info in xitong.items() if info["yuwen"] == high_yuwen]
#             name_low_yuwen=[s for s,info in xitong.items() if info["yuwen"] == low_yuwen]
#             print(f"语文最高分{high_yuwen}姓名{name_high_yuwen}最低分{low_yuwen}姓名{name_low_yuwen}")
#             name_high_shuxue = [a for a, info in xitong.items() if info["shuxue"] == high_shuxue]
#             name_low_shuxue = [a1 for a1, info in xitong.items() if info["shuxue"] == low_shuxue]
#             print(f"数学最高分{high_shuxue}姓名{name_high_shuxue}最低分{low_shuxue}姓名{name_low_shuxue}")
#             name_high_yingyu = [a2 for a2, info in xitong.items() if info["yingyu"] == high_yingyu]
#             name_low_yingyu = [a3 for a3, info in xitong.items() if info["yingyu"] == low_yingyu]
#             print(f"英语最高分{high_yingyu}姓名{name_high_yingyu}最低分{low_yingyu}姓名{name_low_yingyu}")
#             continue
#         case "7":
#             break
#         case _:
#             print("操作错误")
#             continue
# def jiou(a):
#     if a%2==0:
#         return f"{a}是偶数"
#     else:
#         return f"{a}是奇数"
# print(jiou(12))
# print(jiou(10))
# print(jiou(11))
# # def are(r):
# #     area = round(3.14*r*r,1)
# #     zhouchang = round(2*3.14*r,1)
# #     return area, zhouchang
# # print(are(5))
# # print(type(are(5)))
# def are(r):
#     """
#     计算圆的面积周长
#     :param r:半径
#     :return:面积 周长
#     """
#     return r*r*3.14,round(r*2*3.14,1)
# print(are(12))
# area,z=are(12)
# print(area,z)
# help(are)
# help(print)
# def a():
#     print('a')
#     b()
#     print("a1")
# def b():
#     print('b')
#     c()
#     print("b1")
# def c():
#     print('c')
#
# a()
# zimu="aeiouAEIOU"
# def yuan(a):
#     i=0
#     for s in a:
#         if s in zimu:
#             i += 1
#     return i
# a1=input("请输入字符串")
# print("字符串中元音字母个数为",yuan(a1))

# def jisuan(s):
#     """
#     计算分数的最高最低平均分
#     :param s:成绩列表
#     :return: 最高 最低 平均
#     """
#     max_s=max(s)
#     min_s=min(s)
#     avg_s=round(sum(s)/len(s),1)
#     return max_s,min_s,avg_s
# banji=[555,222,111,444,555,666]
# print(jisuan(banji))

