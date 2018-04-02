if __name__ == "__main__":

    l = [1212, "klsdjf", "A", 0.033]

    for e in l:
        print(type(e))

    names = ['A', 'B', 'C', 'D', 'E']
    indexes = range(len(names))

zipped = {}
for index, name in zip(indexes, sorted(names)):
    # print(index,name)
    zipped[index] = name

print(zipped)