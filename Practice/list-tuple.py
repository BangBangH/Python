# !/usr/bin/python
# coding:utf-8

# 有序可變動列表 List 

grades=[12,60,30,20,99]
# grades=grades+[12,33] # 新增數字
# grades[1:4]=[] # 連續刪除列表中從編號1到編號3 4不包含 的資料
# length=len(grades) #取得列表的長度 len(列表資料)
# print(grades[1:4]) # 取1,2,3 不包含4
# grades[0]=55 # 把55放到列表第一個位置
# print(grades[0]) # 第一個資料
grades[2]=9
print(grades)
# 巢狀列表

# data=[[3,4,5],[7,8,9]]
# data[0][0:2]=[9,8,7]
# print(data[1])

# 有序不可變動列表 Tuple 
# data=(3,4,5)
# data[0]=5 # 錯誤：Tuple的資料不可變動
# print(data[0:2])
