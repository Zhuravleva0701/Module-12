#Использование %:
print('В команде Мастера кода участников: %s !' % (5))
team1_num = 5
team2_num = 6
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))



#Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {} !'.format(score_2))

team1_time = 18015.2
team2_time = 18014
print('Волшебники данных решили задачи за {} с !'.format(team1_time))



#Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач')

def result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        challenge_result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        challenge_result = 'Победа команды Волшебники Данных!'
    else:
        challenge_result = 'Ничья!'
    #challenge_result = 'Мастера кода'
    print(f'Результат битвы: победа команды {challenge_result} !')

tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

result()