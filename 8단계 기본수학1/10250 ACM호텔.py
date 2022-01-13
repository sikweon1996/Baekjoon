import sys

T = int(input())

for i in range(T):
    h,w,n = map(int, sys.stdin.readline().split())

    if n%h == 0:
        floor = h
        num = n//h
        print('%s'%(floor*100+num))
    else:
        floor = n % h
        num = n // h + 1
        print('%s' % (floor * 100 + num))
