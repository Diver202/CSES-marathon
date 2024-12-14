def find_kth_digit(k):
    # Define range parameters
    digit_length = 1  # Start with single-digit numbers
    range_start = 1   # First number in the current range
    range_size = 9    # Number of numbers in the current range

    # Determine the range containing the kth digit
    while k > digit_length * range_size:
        k -= digit_length * range_size
        digit_length += 1
        range_start *= 10
        range_size *= 10

    # Determine the exact number and digit
    number = range_start + (k - 1) // digit_length  # Indexing starts from 0
    digit_index = (k - 1) % digit_length

    return int(str(number)[digit_index])



q = int(input())
results = []
for _ in range(q):
    k = int(input())
    results.append(find_kth_digit(k))

print("\n".join(map(str, results)))