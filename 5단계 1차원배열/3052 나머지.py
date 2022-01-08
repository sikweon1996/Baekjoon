
lst = []
lst2 = []
for i in range(0,10):
    a = int(input())
    lst.append(a)
    lst2.append(a%42)
# print(lst)
# print(lst2)

lst3 = sorted(lst2)

hap = 1
for i in range(len(lst3)-1):
    if lst3[i] != lst3[i+1]:
        hap += 1
print(hap)