def solve(arr, N):
    # Variable to store the final answer
    ans = 1

    # Array to store the index of numbers from 1 to N
    indices = [0] * (N + 1)

    # Store the index of all elements of arr[]
    for i in range(N):
        indices[arr[i]] = i

    # If num occurs after (num + 1), increment ans by 1
    for num in range(1, N):
        if indices[num + 1] < indices[num]:
            ans += 1
    return ans

N = int(input())
arr = list(map(int,input().split()))

print(solve(arr, N))