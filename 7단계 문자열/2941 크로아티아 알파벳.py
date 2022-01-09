s = input()

count = 0
minus = 0
for i in range(len(s)-1):
    count += 1
    if (s[i]+s[i+1] == 'c-' or s[i]+s[i+1] =='d-' or s[i]+s[i+1] == 'lj' or
            s[i]+s[i+1] =='nj' or s[i]+s[i+1] =='s=' or s[i]+s[i+1] == 'z=' or
    s[i]+s[i+1] == 'c='  ):
        minus += 1
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2] == 'dz=':
        minus +=1

# print( count+1, minus)
print(count+1-minus)

