class Product():
    def __init__(self, name=str, price=int, quanity=int):
        self.name = name
        self.price = price
        self.quanity = quanity


class Book(Product):
    def __init__(self, name=str, price=int, quanity=int, author=str):
        super().__init__(name, price, quanity)
        self.author = author

    def read(self):
        information_for_book = [
            f'Назва книги - {self.name} '
            f'Автор книги - {self.author} '
            f'Ціна - {self.price} '
            f'Кількість - {self.quanity} '
        ]
        return information_for_book


book1 = Book("Main Kamf", 20, 100, "Adolf Hitler")
book_info = book1.read()
print(book_info)
