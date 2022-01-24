import sys


while True:
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort()
    if lst == [0,0,0]:
        break

    if pow(lst[0],2)+pow(lst[1],2) == pow(lst[2],2):
        print('right')
    else:
        print('wrong')