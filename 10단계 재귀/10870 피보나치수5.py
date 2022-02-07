N= int(input())
if N== 0:
    print(0)
else:
    def f(N):
        result = 1
        if N >= 2:
            result = f(N-1)+f(N-2)
        return result

    print(f(N-1))
