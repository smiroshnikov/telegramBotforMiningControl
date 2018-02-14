# solving python riddles just because i love pyton
ml = [1, 2, 3, 4, 5, 6, 7, 8, "sdf", [1, 2, 3, 4, 5]]

for item in ml:
    if type(item) == list:
        item = item[::-1]

print(ml[::-1])

t = [1, 2, 3, 4, 5]
reverse_t = []
for n in t[::-1]:
    reverse_t.append(n)

print(t)
print(reverse_t)
polindrom_list = t + reverse_t

place = int(len(polindrom_list) / 2)

[polindrom_list[place], polindrom_list[place - 1]] = ["0000" for x in [polindrom_list] if len(polindrom_list) % 2 == 0], 11111

print(polindrom_list)
