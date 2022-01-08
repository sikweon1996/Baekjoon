import sys

N = int(input())

a = list(map(int, sys.stdin.readline().split()))

print('%d %d'%(min(a),max(a)))
