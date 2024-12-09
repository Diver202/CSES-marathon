n = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
median = sticks[n // 2] if n % 2 == 1 else sticks[(n // 2) - 1]
total_cost = sum(abs(stick - median) for stick in sticks)
print(total_cost)
