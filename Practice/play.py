# !/usr/bin/python
# coding:utf-8

import random 

command = input ('是否開始對戰？ 0.開始猜拳 1.逃走 :')



c_choice = random.randint(0,2)

if command == 0:
    choice = int(input ('請問你要選擇什麼？ 0.石頭 1.剪刀 2.布 :'))

    if choice == 0:
        print('我出石頭 !')
        if c_choice == 0:  
              print('你出石頭 , 平手') 
        elif c_choice == 1:
            print('你出剪刀 , you lose')
        elif c_choice == 2:
            print('你出布 , you win')

    elif choice == 1:
        print('我出剪刀 !')
        if c_choice == 0:  
            print('你出石頭 , you win') 
        elif c_choice == 1:
            print('你出剪刀 , 平手')
        elif c_choice == 2:
            print('你出布 , you lose')

    elif choice == 2:
        print('我出布 !')
        if c_choice == 0:   
            print('你出石頭 , you lose') 
        elif c_choice == 1:
            print('你出剪刀 , you win')
        elif c_choice == 2:
            print('你出布 , 平手')

elif command == 1:
    print('遊戲結束') 
