def result(n):
    key = ''
    for i in range(1, n):
        for j in range(1 + i, n + 1):
            if (i+j) % n == 0:
                key += str(i) + str(j)
    return key



for num in range (3, 21):
    print(num, '-', result(num))

num = int(input('Введите число: '))

if num < 3 or num > 20:
    print('Ошибка! Вводите число от 1 до 20')

if 3 <= num <= 20:
    print(f'[{num}] - [{result(num)}')