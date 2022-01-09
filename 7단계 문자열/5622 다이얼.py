S = input()

word2 = {
    1 : '',
    2 : 'ABC',
    3 : 'DEF',
    4 : 'GHI',
    5 : 'JKL',
    6 : 'MNO',
    7 : 'PQRS',
    8 : 'TUV',
    9 : 'WXYZ'
}
hap = 0
for key, value in word2.items():
    for i in range(len(S)):
        if S[i] in value:
            # print(value, key+1)
            hap += key+1
print(hap)