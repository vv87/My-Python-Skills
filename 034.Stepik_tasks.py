"""Напишите программу, которая принимает на стандартный вход список игр футбольных 
команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
"""


games = int(input())
teams_and_stats = {}
for game in range(games):
    game_stats = input().strip().split(';')

    team1, team2 = game_stats[0], game_stats[2]
    score1, score2 = int(game_stats[1]), int(game_stats[3])
    scores = (score1, score2)
    positions = {team1: 1, team2: 2}
    for team, score in {team1: score1, team2: score2}.items():
        if team in teams_and_stats:
            if score > scores[positions[team]-2]:
                teams_and_stats[team][0] = teams_and_stats[team][0]+1
                teams_and_stats[team][1] = teams_and_stats[team][1]+1
                teams_and_stats[team][4] = teams_and_stats[team][4]+3
            elif score == scores[positions[team]-2]:
                teams_and_stats[team][0] = teams_and_stats[team][0]+1
                teams_and_stats[team][2] = teams_and_stats[team][2]+1
                teams_and_stats[team][4] = teams_and_stats[team][4]+1
            else:
                teams_and_stats[team][0] = teams_and_stats[team][0]+1
                teams_and_stats[team][3] = teams_and_stats[team][3]+1
        else:
            if  score > scores[positions[team]-2]:
                teams_and_stats[team] = [1, 1, 0, 0, 3]
            elif score == scores[positions[team]-2]:
                teams_and_stats[team] = [1, 0, 1, 0, 1]
            else:
                teams_and_stats[team] = [1, 0, 0, 1, 0]

for team in teams_and_stats:
    print(team, end=':'), print(*teams_and_stats[team])
