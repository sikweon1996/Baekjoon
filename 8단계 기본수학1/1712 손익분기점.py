import sys

S = list(map(int, sys.stdin.readline().split()))

if (S[1] > S[2] or S[0]==0 or S[1]-S[2]==0):
    print('-1')
else:
    if S[0] != 0:
        a = S[0]//(S[2]-S[1])
        print('%d'%(a+1))

