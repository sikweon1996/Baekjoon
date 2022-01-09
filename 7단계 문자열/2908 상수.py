import sys

S = sys.stdin.readline().split()

a1 = S[0]
a2 = S[1]
# print(a1, a2)
s1 ,s2 ='',''
for i in range(len(a1)):
    s1 += a1[2-i]
    s2 += a2[2-i]
if int(s1) > int(s2):
    print(s1)
else:
    print(s2)