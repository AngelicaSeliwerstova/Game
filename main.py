import os
from sys import argv

start=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
def victory(start):
    for i in range(len(start)):
        for j in range(3):
            if start[i][0]==start[i][1]==start[i][2]!=' ' or start[0][j]==start[1][j]==start[2][j]!=' ' or start[0][0]==start[1][1]==start[2][2]!=' ' or start[2][0]==start[1][1]==start[0][2]!=' ' :
                return True
sight = 1
while True:
    try:
        row, column = map(str, input().split())
        if start[int(row) - 1][int(column) - 1] == ' ':
            start[int(row) - 1][int(column) - 1] = 'x' if sight == 1 else '0'
            sight = (sight + 1) % 2
            if victory(start):
                print("Victory")
                for i in range(3):
                    print(' ' + ' | '.join(start[i]))
                    if i < 2:
                        print('---+---+---')
                break
        else:
            print("Введите еще раз:")
            continue
    except:
        print("Введите еще раз:")
        continue


    for i in range(3):
        print(' ' + ' | '.join(start[i]))
        if i < 2:
            print('---+---+---')



