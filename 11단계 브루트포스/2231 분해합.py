
N = int(input())
while True:
    hap = 0
    if hap >= N:
        print(hap)
        break
    num = 1
    a = str(num)

    for i in range(len(a)):
        hap += (num+int(a[i]))
    num += 1