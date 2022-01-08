S = input()

# 입력값 아스키코드 변환 후 빼기96
list1 = []
for i in range(len(S)):
    list1.append(ord(S[i])-97)
for i in range(len(list1)):
    if list1[i] == list1[i+1]:
        print('zz')
print(list1)
list1.sort()
print(list1)

list2 = []
for i in range(0,26):
    if i in list1:
        list2.append('O')
    else:
        list2.append('-1')
for i in range(len(list2)):
    if list2[i] == 'O':
        del(list2[i])
        list2.insert(i,)


print(list2)
