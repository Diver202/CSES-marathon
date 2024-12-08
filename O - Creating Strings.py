import itertools

target = input()

stringset = set(''.join(perm) for perm in itertools.permutations(target))

sorted_strings = sorted(stringset)

print(len(sorted_strings))

for perm in sorted_strings:
    print(perm)

