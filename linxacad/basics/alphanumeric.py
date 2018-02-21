import string

x = "ksdjf;lsjkdf 126786 slkj <<<>> 12§1  "

for char in x:
    if char not in string.ascii_letters:
        print(char)

# DONT DO THIS IN PYTHON, this is fucked up python , this is not python
# spaces = 0
# for c in x:
#     if (' ' in x):
#         print("space found ", spaces)
#         spaces += 1


print(x.count(" "))
print(x[13:])
print (x[13:].find(" "))