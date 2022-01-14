import sys
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

#2층 3호


    floor, number = k , n
    # 2층 => 변수 2개 필요
    a,b,c,d,e,f,g,h,i,j,k,l,m,n = 0,0,0,0,0,0,0,0,0,0,0,0,0,0

    list1 = []
    # 3호 => 범위 1부터 4까지
    for num in range(1,number+1):
        a += num
        b += a
        c += b
        d += c
        e += d
        f += e
        g += f
        h += g
        i += h
        j += i
        k += j
        l += k
        m += l
        n += m
    lst = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
    print(lst[floor-1])
