def solve(customers):
    # Create separate lists for arrival and departure times
    arrival = sorted([i[0] for i in customers])
    departure = sorted([i[1] for i in customers])

    n = len(arrival)
    i = 0
    j = 0
    current_customers = 0
    max_customers = 0

    # Traverse both arrays and update max_customers
    while i < n and j < n:
        # Customer arrives before or exactly at the departure of 
        # the previous customer
        if arrival[i] <= departure[j]:
            current_customers += 1
            i += 1
        # Customer arrives after the departure of the previous customer
        else:
            j += 1
            current_customers -= 1
        max_customers = max(max_customers, current_customers)

    return max_customers


customers = []
for i in range(int(input())):
    customers.append(list(map(int,input().split())))
print(solve(customers))
