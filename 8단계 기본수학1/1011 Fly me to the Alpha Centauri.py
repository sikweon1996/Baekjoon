import sys

N = int(input())
a =0
b = 0
# max_distance = 0
for i in range(N):
    x,y = map(int, sys.stdin.readline().split())
    distance = y-x
    max_distance = 0
    for i in range(pow(2,31)):
        if i%2 != 0:
            max_distance += (i+1)//2
        else:
            max_distance += i//2

        #print(max_distance)
        if max_distance >= distance:
            print(i)
            break