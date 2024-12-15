n = int(input())
count = 0
while n!=0:
    digit = int(max(str(n)))
    n = n - digit
    count+=1
print(count)
