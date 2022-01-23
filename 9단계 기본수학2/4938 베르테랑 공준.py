import sys

lst = []
for i in range(1,2*123456+1):
    if i == 1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        lst.append(i)
#print(lst)

while True:

    N = int(input())
    if N == 0:
        break
    count = 0
    for num in lst:
        if N < num <= 2*N:
            count += 1
    print(count)



