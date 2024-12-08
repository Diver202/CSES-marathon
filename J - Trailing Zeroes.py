def solve(N):
    if N == 0:
        return 0
    return N // 5 + solve(N // 5)

print(solve(int(input())))