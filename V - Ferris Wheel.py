n,x = map(int,input().split())
weights = list(map(int,input().split()))
weights.sort()
ans = 0
l,h = 0, n-1
while h >= l:
    # If the heaviest and lightest child can fit in a gondola, then pair them up
    if weights[l] + weights[h] <= x:
        ans += 1
        l += 1
        h -= 1
    # If the heaviest and lightest child cannot fit in a gondola,
    # then put the heaviest child in a separate gondola
    else:
        ans += 1
        h -= 1

print(ans)