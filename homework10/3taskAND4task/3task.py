import random
import csv


def simulation(list_name, rounds):
    player_scores = []
    for player in list_name:
        scores = [random.randint(0, 1000) for _ in range(rounds)]
        player_scores.extend([(player, score) for score in scores])
    return player_scores


list_name = [
    'Джож',
    'Люк',
    'Кейт',
    'Марк',
    'Мері',
    'Джош'
]
rounds = 100
player_scores = simulation(list_name, rounds)
with open('player_scores.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Player name', 'Score'])
    for player, score in player_scores:
        csv_writer.writerow([player, score])
print("Результати гри збережено у файл player_scores.csv")
