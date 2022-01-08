
a = int(input())
b = int(input())
c = int(input())

lst = list(str(a*b*c))


for i in range(0,10):
    print(lst.count('%d'%i))

