import time


def limit_func(max_calls, period_seconds):
    def decorator(func):
        call_history = []

        def wrapper(*args, **kwargs):
            current_time = int(time.time())
            cutoff_time = current_time - period_seconds
            call_history[:] = [call_time for call_time
                               in call_history if call_time > cutoff_time]
            if len(call_history) < max_calls:
                call_history.append(current_time)
                return func(*args, **kwargs)
            else:
                remainder = 60 - (current_time - call_history[-1])
                print('Функцію більше не можна викликати.'
                      f'Спробуй через {remainder} секунд')
        return wrapper
    return decorator


@limit_func(max_calls=2, period_seconds=60)
def function():
    print('Функція яку можна викликати 2 рази за 60 секунд')


n = int(input('Скільки разів ти хочеш викликати функцію: '))
for i in range(n):
    function()
