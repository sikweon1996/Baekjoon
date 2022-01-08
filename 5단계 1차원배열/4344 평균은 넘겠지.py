import sys

C = int(input())
for i in range(C):

    a = sys.stdin.readline().split()
    score = []
    for i in range(len(a)):
        score.append(int(a[i]))

    hap = 0
    for i in range(1,len(score)):
        hap += score[i]
    average = hap/score[0]

    count = 0
    for i in range(len(score)):
        if score[i] > average:
            count += 1

    b =  ( count/ score[0] ) * 100
    print('%.3f'%b+'%')

# c = round(b, 3)
# list1 = list(str(c))
# # print(list1)
# for i in range(len(list1)):
#     if len(list1) < 6:
#         list1.append('0')
# # print(list1)
# list1.append('%')
# # print(list1)
# d = ''
# for i in range(len(list1)):
#     d += list1[i]
# print(d)