import lorem


def text_generator():
    text = lorem.text()
    return text


def create_txt_file(file_name):
    generated_text = text_generator()
    with open(file_name, 'w') as file:
        file.write(generated_text)


def copy_to_uppercase(first_file_name, second_file_name):
    with open(first_file_name, 'r') as first_file:
        content = first_file.read()
    content_upper = content.upper()
    with open(second_file_name, 'w') as second_file:
        second_file.write(content_upper)


file_name = input("Введи назву файлу, який ти хочеш створити: ")
create_txt_file(file_name + '.txt')
print(f"Файл '{file_name}' створено та заповнено текстом.")
first_file_name = input("Введіть назву першого файлу: ")
second_file_name = input("Введіть назву другого файлу: ")
copy_to_uppercase(first_file_name + '.txt', second_file_name + '.txt')
print(f"Вміст файлу: '{first_file_name}' скопійовано у верхньому регістрі"
      " до файлу: '{second_file_name}'.")
