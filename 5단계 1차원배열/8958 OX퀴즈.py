import sys

N = int(input())
for i in range(N):
    a = list(sys.stdin.readline())

    count = 0
    hap = 0
    for i in range(len(a)-1):
        if a[i] == 'O':
            count += 1
            hap += count

        if a[i] == 'X':
            count = 0
            continue
    print(hap)


