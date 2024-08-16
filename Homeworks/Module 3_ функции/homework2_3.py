def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(2, 8, 6)
print_params(4, b='hello', c='hello')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [8, 'one', True]
print_params(*values_list)

values_dict = {'a':1, 'b': 'строка', 'c': True}
print_params(**values_dict)

values_list_2 = ['one', 2]
print_params(*values_list_2, 42)