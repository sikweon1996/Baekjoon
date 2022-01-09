import sys

N = int(sys.stdin.readline())
s = str(N)
#print(len(s))
hap = 0
count = 0
num = 0
list1 = [1]
#print( N// ( 6** (len(s)-1) ) )
for i in range( 3**len(s)):
    count += 1
    hap = hap+count
    num = 6*hap + 1
    list1.append(num)
#print(list1)
#print(len(list1))
for i in range(len(list1)-1):
    if ( N > list1[i] and N <= list1[i+1]):
        print('%d'%(i+2))
if N == 1:
    print('1')