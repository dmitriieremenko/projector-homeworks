import random
import string


def generator():
    random_int = random.randint(1, 100)
    return random_int


def main():
    naming_all = string.ascii_uppercase
    for file_naming in naming_all:
        file_name = f"{file_naming}.txt"
        random_int = generator()
        with open(file_name, 'w') as file:
            file.write(str(random_int))
    with open('summary.txt', 'w') as summary_file:
        for char in naming_all:
            file_name = f"{char}.txt"
            with open(file_name, 'r') as file:
                number = file.read().strip()
                summary_file.write(f"{file_name}: {number}\n")
        print("Файл 'summary.txt' був створений!")


main()
