# Напишіть декоратор, який гарантує, що функцію можуть викликати лише користувачі з певною роллю. Кожна функція повинна мати аргумент user_type зі строковим типом в kwargs. Приклад:
@is_admin
def show_customer_receipt(user_type: str):
    # Some very dangerous operation

show_customer_receipt(user_type='user')
> ValueError: Permission denied

show_customer_receipt(user_type='admin')
> function pass as it should be