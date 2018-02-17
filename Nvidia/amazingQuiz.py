CPU = "Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz 3.20GHz "

x = CPU.split(" ")
# print(x)
for element in x:
    b = False
    if "Hz" in element:
        print(element)
        b = True
    if b:
        break
