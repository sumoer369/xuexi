# students = (
#     ("S001", "王林", 85, 92, 78),
#     ("S002", "李慕婉", 92, 88, 95),
#     ("S003", "十三", 78, 85, 82),
#     ("S004", "曾牛", 88, 79, 91),
#     ("S005", "周轶", 95, 96, 89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "遁天", 66, 59, 72)
# )
# print("学号   姓名      语文  数学  英语  总分  平均分")
# # for s in students:
# #     zonfen = s[2]+s[3]+s[4]
# #     pingjun = zonfen/3
# #     print(f"{s[0]}\t{s[1]}\t{s[2]}  {s[3]}  {s[4]}    {zonfen}    {pingjun:.1f}")
# for id, name, yuwen,shuxue,yinyu in students:
#     zonden = yuwen+shuxue+yinyu
#     pinjun = zonden/3
#     print(f"学号{id}，姓名{name}，语文{yuwen}，数学{shuxue}，英语{yinyu}")
# yuwen = [s[2] for s in students]
# shuxue = [s[3] for s in students]
# yinyu = [s[4] for s in students]
# print(min(yuwen),max(yuwen),sum(yuwen)/len(yuwen))
# for a in students:
#     zon = a[2]+a[3]+a[4]
#     pingjun = zon/3
#     if pingjun > 90:
#         print(f"{a}")

