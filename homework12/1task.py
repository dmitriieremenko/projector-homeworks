def is_admin(func):
    def wrapper(**kwargs):
        if kwargs.get('user_type') == 'admin':
            return func(**kwargs)
        else:
            return 'ValueError: Permission denied'
    return wrapper


@is_admin
def show_customer_receipt(user_type: str):
    return 'sudo rm -rf this world. You are destroy this world'


result1 = show_customer_receipt(user_type='user')
print(f'Ви user. Результат виконання задачі: {result1}')
result2 = show_customer_receipt(user_type='admin')
print(f'Ви admin. Результат виконання задачі: {result2}')
