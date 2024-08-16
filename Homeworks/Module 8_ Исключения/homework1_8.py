def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        if type(a) == str and type(b) == float or type(b) == int:
            return a + str(b)
        if isinstance(a, float) or isinstance(a, int) and isinstance(b, str): #просто разными способами попробовала
            return str(a) + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
