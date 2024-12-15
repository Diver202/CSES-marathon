def solve(A, B, N, M, K):
    # Sort both the arrays in ascending order
    A.sort()
    B.sort()

    # Maintain two pointers to store the current value
    # in both the arrays
    ptrA, ptrB, ans = 0, 0, 0
    while ptrA < N and ptrB < M:
        # Check if the applicant at index ptrA can
        # purchase the apartment at index ptrB
        if abs(A[ptrA] - B[ptrB]) <= K:
            # Increase the number of purchases
            ans += 1
            ptrA += 1
            ptrB += 1
        # If the current applicant's demand is too
        # small, move to the next applicant
        elif A[ptrA] < B[ptrB]:
            ptrA += 1
        # If the current apartment's size is too small,
        # move to the next apartment
        else:
            ptrB += 1
    return ans

n,m,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(solve(A,B,n,m,k))
