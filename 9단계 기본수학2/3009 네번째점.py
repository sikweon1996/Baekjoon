import sys

x_list = []
y_list = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    x_list.sort()
    y_list.append(y)
    y_list.sort()

lst = []
for i in range(len(x_list)):
    if x_list[0] == x_list[1]:
        lst.append(x_list[2])
        break
    else:
        lst.append(x_list[0])
        break
for j in range(len(y_list)):
    if y_list[0] == y_list[1]:
        lst.append(y_list[2])
        break
    else:
        lst.append(y_list[0])
        break

print('%d %d'%(lst[0], lst[1]))
