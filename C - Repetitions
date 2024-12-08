def solve(S):
    ans = 1
    count = 1

    for i in range(1, len(S)):
        if S[i] == S[i - 1]:
            count += 1
        else:
            count = 1

        ans = max(ans, count)

    return ans

print(solve(input()))