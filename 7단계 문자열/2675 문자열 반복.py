import sys

T = int(input())
for i in range(T):
    S = sys.stdin.readline().split()
    s1 = ''
    for i in range(len(S[1])):
        # for j in range(len(S[1])):
        s1 += int(S[0])*S[1][i]
    print(s1)
