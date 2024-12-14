from sortedcontainers import SortedList

def concert_tickets(n, m, tickets, customers):
    # Create a SortedList from ticket prices
    sorted_tickets = SortedList(tickets)
    
    results = []
    for t in customers:
        # Find the first ticket that is <= t (max price the customer can pay)
        idx = sorted_tickets.bisect_right(t) - 1
        
        if idx >= 0:  # Valid ticket exists
            results.append(sorted_tickets[idx])
            sorted_tickets.pop(idx)  # Remove the ticket from the SortedList
        else:
            results.append(-1)  # No valid ticket available
    
    return results

# Input reading
n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

# Compute results
results = concert_tickets(n, m, tickets, customers)

# Output results
print("\n".join(map(str, results)))
