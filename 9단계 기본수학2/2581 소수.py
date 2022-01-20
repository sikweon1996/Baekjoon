import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

lst = []
hap = 0
for i in range(M, N+1):
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
            if count == 2 and j>=i:
                lst.append(j)
                hap += j
                break

if len(lst) < 1:
    print(-1)
else:
    print(hap)
    print(lst[0])
