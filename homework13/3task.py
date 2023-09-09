class Car:
    def __init__(self, brand: str, model: str, year: int, speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0
        return self.speed

    def display_speed(self):
        return self.speed


def user_interface(car):
    while True:
        try:
            first_message = int(input('Привіт! Обери операцію, яку'
                                      'ти хочеш зробити з '
                                      'автомобілем (1 - газанути на 5 км.'
                                      ', 2 - притормозити на 5 км., 3 - '
                                      'показати швидкість, 0 - вийти): '))
            if first_message == 1:
                car.accelerate()
            elif first_message == 2:
                car.brake()
            elif first_message == 3:
                print('Поточна швидкість:', car.display_speed())
            elif first_message == 0:
                break
            else:
                print('Тобі потрібно обрати 1, 2, 3 або 0!')
        except ValueError:
            print('Введіть ціле число для вибору операції.')


car1 = Car('Volkswagen', 'Golf V', 2008, 0)
user_interface(car1)
