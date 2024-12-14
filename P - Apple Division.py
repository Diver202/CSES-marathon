# # Brute Force method
# def mindiff(array):
#     n = len(array)
#     answer = 10**9 + 1
#     tot = sum(array)

#     # Iterate through all possible bitmasks (2^n combinations)
#     for mask in range(1 << n):  # 1 << n is 2^n
#         curr = 0
#         for i in range(n):
#             # Check if the i-th bit is set in the mask
#             if mask & (1 << i):
#                 curr += array[i]
#         diff = tot - curr
#         minm = abs(diff - curr)
#         answer = min(minm,answer)

#     return answer

# n = int(input())
# print(mindiff(list(map(int,input().split()))))

def solve(idx, arr, sum1, sum2, N):
    # If we have reached the end, return the difference
    # between the sums
    if idx == N:
        return abs(sum1 - sum2)

    # Choose the current apple in group 1
    choose = solve(idx + 1, arr, sum1 + arr[idx], sum2, N)

    # Choose the current apple in group 2
    not_choose = solve(idx + 1, arr, sum1, sum2 + arr[idx], N)

    # Return the minimum of both the choices
    return min(choose, not_choose)


N = int(input())
arr = list(map(int,input().split()))

# Call the recursive function to find the minimum
# difference between both the groups
ans = solve(0, arr, 0, 0, N)
print(ans)

