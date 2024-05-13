# Использование %
team1_num = 5
team1_total = 5
team2_num = 6

team1_info = "В команде Мастера кода участников: %d!" % team1_num
total_info = "Итого сегодня в командах участников: %d и %d!" % (team1_num, team2_num)

print(team1_info)
print(total_info)

# Использование format()
score_2 = 42
team1_time = 18015.2

score_info = "Команда Волшебники данных решила задач: {}!".format(score_2)
time_info = "Волшебники данных решили задачи за {} с!".format(team1_time)

print(score_info)
print(time_info)

# Использование f-строк
score_1 = 40
score_2 = 42
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 350.4


score_summary = f"Команды решили {score_1} и {score_2} задач."
result_info = f"Результат битвы: {challenge_result}"
task_info = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"


print(score_summary)
print(result_info)
print(task_info)
