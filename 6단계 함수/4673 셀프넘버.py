def produce(a):
    b = list(str(a))
    b.append(a)
    # print(b)

    hap = 0
    for i in range(len(b)):
        hap += int(b[i])
    return hap
    # print(hap)


list1 = []
for i in range(1, 10000):
    a = i
    list1.append(produce(a))
list2 = sorted(list1)
# print(list2)

list3 = []
for i in range(1, 10001):
    list3.append(i)

for i in list3:
    if i not in list2:
        print(i)