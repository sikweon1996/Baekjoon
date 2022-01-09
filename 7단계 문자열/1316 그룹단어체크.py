N = int(input())

hap = 0
for i in range(N):

    S = input()
    if len(S) == 1:
        hap +=1
    else:

        list1 =[]
        s1 = ''
        for i in range(len(S)-1):
            s1 += S[i]
            if S[i] != S[i+1]:
                list1.append(s1)
                s1 = ''
        list1.append(S[len(S)-1])
        #print(list1)

        list2 = []
        for i in range(len(list1)):
            list2.append(list1[i][0])
        #print(list2)
        list3 = sorted(list2)
        #print(list3)

        minus = 0
        for i in range(len(list3)-1):
            if list3[i] == list3[i+1]:
                minus += 1

        if minus > 0 :
            hap += 0
        else:
            hap += 1

print(hap)

