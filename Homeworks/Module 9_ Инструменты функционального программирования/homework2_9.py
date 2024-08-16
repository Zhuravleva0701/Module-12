# старый вариант
def square(x):
    return x ** 2


def odd_numbers(x):
    return x % 2

list_1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

list_2 = map(square, filter(odd_numbers, list_1))
print(list(list_2))

# новый вариант

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
print(list(first_result))

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(list(second_result))

lst = first_strings + second_strings

third_result = {item: len(item) for item in lst if len(item) % 2 == 0}
print(list(third_result))