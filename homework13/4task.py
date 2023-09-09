class Robot:
    def __init__(self, orientation: str, position_x: int, position_y: int):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, direction: str, steps: int):
        if direction == 'вліво':
            self.position_x -= steps
        elif direction == 'вправо':
            self.position_x += steps
        elif direction == 'вгору':
            self.position_y += steps
        elif direction == 'вниз':
            self.position_y -= steps

    def display_position(self):
        print(f"Поточна позиція робота:"
              f"По осі X - ({self.position_x})"
              f", По осі Y - ({self.position_y})")


def user_interface(robot):
    while True:
        try:
            print('Оберіть операцію:')
            print('1 - Іти вліво')
            print('2 - Іти вправо')
            print('3 - Іти вгору')
            print('4 - Іти вниз')
            print('5 - Показати позицію')
            print('0 - Вийти')
            choice = int(input('Ваш вибір: '))
            if choice == 1:
                steps = int(input('Введіть кількість кроків: '))
                robot.move('вліво', steps)
            elif choice == 2:
                steps = int(input('Введіть кількість кроків: '))
                robot.move('вправо', steps)
            elif choice == 3:
                steps = int(input('Введіть кількість кроків: '))
                robot.move('вгору', steps)
            elif choice == 4:
                steps = int(input('Введіть кількість кроків: '))
                robot.move('вниз', steps)
            elif choice == 5:
                robot.display_position()
            elif choice == 0:
                break
            else:
                print('Тобі потрібно обрати одну з операцій (0-5)!')
        except ValueError:
            print('Введіть ціле число для вибору операції.')


robot1 = Robot('robot_stop', 0, 0)
user_interface(robot1)
