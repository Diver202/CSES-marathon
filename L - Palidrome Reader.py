frequency = {}
word = input()
for letter in word:
    if letter not in frequency:
        frequency[letter]=1
    else:
        frequency[letter]+=1
odds = 0
odd = ""
for letter in frequency:
    if frequency[letter]%2!=0:
        odds+=1
        odd = letter
    if odds == 2:
        print("NO SOLUTION")
        exit()
halfstring = ""
for letter in frequency:
    halfstring += letter*(frequency[letter]//2)
print(halfstring + odd + halfstring[::-1])
