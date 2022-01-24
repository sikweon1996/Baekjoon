import sys

x,y,w,h = map(int, sys.stdin.readline().split())

lst = [x,y,w-x,h-y]
lst.sort()
print(lst[0])