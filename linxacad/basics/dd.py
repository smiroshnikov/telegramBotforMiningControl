from pprint import pprint

ages = {"Kevin": 134, "Alex": 25, "Bob": 26}

for k, v in ages.items():
    print(k, v)

ages['Keyla'] = 242

print(ages.values())
print(ages.items())

weight = dict(kevin=160, kyle=230) # another way to create a dictionary
print(weight.items())

colors = dict([('kevin', 'green'), ('bob', 'blue')]) # another way

print(colors.items())

print(colors['bob'])
