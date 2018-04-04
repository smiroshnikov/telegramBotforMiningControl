if __name__ == "__main__":

    l = [1212, "klsdjf", "A", 0.033]

    for e in l:
        print(type(e))

    # something cool that will probably be asked during interview
    # a way to quickly store key , value , when everyting is sorted and indexed

    letters = ['R', 'A', 'B', 'X', 'E', 'Z', 'C']

    indexes = range(len(letters))  # creates an range object that can be used later in zip

    zipped = {}  # dictonary we want to create
    for index, letter in zip(indexes, sorted(letters)):
        zipped[index] = letter  # appending to dict
    print(zipped)

    names = ['John Smith', 'Adam Dom', 'Tim Cook', 'Sundar Pichai', 'Elon Musk', 'Sebastian Thrun', 'Steve Jobs', 'Bill Gates', 'Sergey Miroshnikov']
    for name in names:
        print(name.replace(' ', '-'))

    last_names = []
    for name in names[:5]:
        full_name = name.split(' ')
        print(full_name[0])
        print(full_name[-1])
        last_names.append(full_name[-1])

    print(last_names)

    # sets contains distinct elements
    last_names.append("Momi")
    last_names.append("Momi")
    last_names.append("Momi")
    last_names.append("Momi")
    last_names.append("Momi")
    last_names.append("Momi")
    print(last_names)

    ml = [lname for lname in last_names]  # same as ->  for lname in last_names : lname.append(lname)
    print(ml)
    unique_last_names = set(last_names)
    print(unique_last_names)

    print('No. of records - {}\nNo. of unique last names - {}'.format(len(last_names), len(unique_last_names)))


    # type annotations
    def my_add(a: int, b: int) -> int:
        return a + b


    print(my_add(0.1, 0.3))
