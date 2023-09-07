def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as kwargs:
            return f"KeyError no such key as {kwargs}"
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['key'])


result1 = some_function_with_risky_operation({'foo': 'bar'})
print(result1)
result2 = some_function_with_risky_operation({'key': 'bar'})
print(result2)
