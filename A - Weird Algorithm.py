N = int(input())
while N!=1:
    print(int(N),end=' ')
    if N%2 == 0:
        N = N/2
    else:
        N = 3*N+1
print(1)