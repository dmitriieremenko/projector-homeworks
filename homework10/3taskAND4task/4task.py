import csv


def sort_and_write_scores():
    with open('player_scores.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        player_scores = list(csv_reader)
    highest_scores = {}
    for player, score in player_scores:
        score = int(score)
        highest_scores[player] = max(highest_scores.get(player, 0), score)
    sorted_scores = [(player, score) for player, score
                     in highest_scores.items()]
    sorted_scores.sort(key=lambda x: x[1], reverse=True)
    with open('high_scores.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerow(['Player name', 'Highest score'])
        csv_writer.writerows(sorted_scores)


sort_and_write_scores()
