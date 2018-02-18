x, y, z = 0, 0, 1

if x == 1 or y == 1 or z == 1:
    print("passed")
    y = 2

if 2 in (x, y, z):
    print("inside")
else:
    print("outside")

if x or y or z:
    print(f"requirement :{True}")

if any((x, y, z)):
    print("at least one true")
