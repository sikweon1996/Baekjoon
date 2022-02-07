N = int(input())

def fact(N):
    hap = 1
    if N>0:
        hap = N * fact(N-1)
    return hap

print(fact(N))