def permutation(N):

    if N == 2 or N == 3:
        print("NO SOLUTION")
        return

    for i in range(2, N + 1, 2):
        print(i)

    for i in range(1, N + 1, 2):
        print(i)
N = int(input())
permutation(N)