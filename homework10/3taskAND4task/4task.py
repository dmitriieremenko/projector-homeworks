import csv


def sort_and_write_scores():
    with open('player_scores.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        player_scores = list(csv_reader)
    sorted_scores = sorted(player_scores, key=lambda x: int(x[1]),
                           reverse=True)
    with open('high_scores.csv', 'w', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerow(['Player name', 'Highest score'])
        csv_writer.writerows(sorted_scores)


sort_and_write_scores()
