import sys

a,b,v = map(int, sys.stdin.readline().split())

if a-b==1:
    print(v-b)
else:
    if (v-b)%(a-b) == 0:
        print( ((v-a)//(a-b))+1 )
    else:
        print( ((v-a)//(a-b))+2 )
