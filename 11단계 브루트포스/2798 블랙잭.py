import sys

N,M = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))

#print(lst)
lst2 = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            if lst[i]+lst[j]+lst[k] <= M:
                lst2.append(lst[i]+lst[j]+lst[k])

#print(len(lst2))
print(max(lst2))