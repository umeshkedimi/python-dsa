class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            discount_amount = (self.price * discount_percentage) / 100
            self.price -= discount_amount
        else:
            raise ValueError("Discount percentage must be between 0 and 100")
        
book_1 = Book("1984", "George Orwell", 15.99)
book_1.apply_discount(10)
print(f"Title: {book_1.title}, Author: {book_1.author}, Price: ${book_1.price:.2f}")