import random
import csv


def random_score():
    return random.randint(0, 1000)


def simulation(list_name):
    player_scores = []
    for player in list_name:
        total_score = 0
        for _ in range(100):
            round_score = random_score()
            total_score += round_score
        player_scores.append((player, total_score))
    return player_scores


list_name = [
    'Джож',
    'Люк',
    'Кейт',
    'Марк',
    'Мері',
    'Джош'
]
player_scores = simulation(list_name)
with open('player_scores.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Player name', 'Score'])
    for player, score in player_scores:
        csv_writer.writerow([player, score])
print("Результати гри збережено у файл player_scores.csv")
