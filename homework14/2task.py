class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name: str, cuisine: str, menu: dict, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, name_food: str, quantity: int):
        if name_food in self.menu:
            price_item = self.menu[name_food]
            if quantity > 0 and quantity <= self.menu[name_food]:
                total_cost = price_item * quantity
                self.menu[name_food] -= quantity
                return (
                    f"Загальна вартість замовлення '{name_food}'"
                    f"({quantity} порцій): {total_cost} грн."
                )
            else:
                return (
                    f"Некоректна кількість порцій '{name_food}'"
                    "для замовлення."
                )
        else:
            return f"Страва '{name_food}' не доступна у меню."


menu = {
    'Гамбургер': 50,
    'Картопля фрі': 30,
    'Кола': 20
}
fast_food_restaurant = FastFood("McDonalds", "Фастфуд", menu, True)
print(fast_food_restaurant.order('Гамбургер', 2))
print(fast_food_restaurant.order('Піца', 1))
print(fast_food_restaurant.order('Картопля фрі', 50))
