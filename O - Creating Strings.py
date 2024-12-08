#getting wrong answer
import itertools
target = input()
stringset = set()
for perm in itertools.permutations(target):
    stringset.add(''.join(perm))
print(len(sorted(stringset)))
[print(perm) for perm in stringset]
