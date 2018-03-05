def my_func(x, y, z):
    print(x, y, z)


tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

my_func(*tuple_vec)

my_func(*dict_vec)
my_func(**dict_vec)
