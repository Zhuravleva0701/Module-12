data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]


def new_data_structure(data_structure):
    for i in data_structure:
        new_string = ''
        if type(i) == int:
            var = type(str) == i
            new_string = var
        elif type(i) == tuple:
            var = type(str) == i
            new_string = var
        elif type(i) == dict:
            var = type(str) == i
            new_string = var
        elif type(i) == set:
            var = type(str) == i
            new_string = var
        elif type(i) == list:
            var = type(str) == i
            new_string = var
        elif type(i) == str:
            var = type(str) == i
            new_string = var

    return new_string

result = new_data_structure(data_structure)

print(result)