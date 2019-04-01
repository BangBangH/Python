# !/usr/bin/python
# coding:utf-8
# 判斷式
# if True:
#    print("True perform")
# else:
#    print("False prform")
# x=input("請輸入數字：") # 基本輸入為字串型態,取得使用者輸入
# x=int(x) # 轉換為整數,將字串型態轉換成數字型態
# if x<100:
#    print("小於100")
# elif x>100:
#    print("大於100")
# else:
#    print("小於等於 100")cl
# 四則運算
# float 浮點運算
input=raw_input 
n1=float(input("輸入第一個數字:"))
n2=float(input("輸入第二個數字:"))
x=input("請輸入運算")
if x=="+":
    print(n1+n2)
elif x=="-":
    print(n1-n2)
elif x=="*":
    print(n1*n2)
elif x=="/":
    print(n1/n2)
else:
    print("False")