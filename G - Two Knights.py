def two_knights(K):

    total_ways = ((K * K) * ((K * K) - 1)) // 2


    attacking_ways = 4 * (K - 1) * (K - 2)

    ans = total_ways - attacking_ways

    return ans


N = int(input())


for K in range(1, N + 1):
    print(two_knights(K))