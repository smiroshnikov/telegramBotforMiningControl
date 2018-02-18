"""
solution of common issue to sort a dictionary
"""
# solution 1
d = {'a': 11, 'b': 3, 'ac': 24,
     'bd': -584, 'ce': 0, 'f': 0,
     'g': -587}
print(sorted(d.items(), key=lambda x: x[1]))

sortedD = []
for k, v in (sorted(d.items(), key=lambda x: x[1])):
    sortedD.append((k, v))

for item in sortedD:
    print(item)
# solution 2

import operator

f = sorted(d.items(), key=operator.itemgetter(0))

print(f"sorted by key{f}")

f = sorted(d.items(), key=operator.itemgetter(1))
print(f"sorted by value{f}")
