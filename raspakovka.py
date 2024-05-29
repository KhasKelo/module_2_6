def print_params(a=1, b='строка', c = True):
    print(a, b, c)

values_list = [4, 'Grozny', True]
values_dict = {'a': 3, 'b': 'Moscow', 'c': False }

values_list_2 = [65, 'Marakesh']

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2,42)