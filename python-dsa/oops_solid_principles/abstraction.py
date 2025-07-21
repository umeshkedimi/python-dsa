class CoffeOrder:
    def __init__(self, customer_name: str, drink_type: str, size: str):
        self.customer_name = customer_name
        self.drink_type = drink_type
        self.size = size
        self.__price = 5.0

    # Public method to display order summary
    def get_order_summary(self) -> str:
        return f"Order for {self.customer_name}: {self.size} {self.drink_type} - ${self.__price:.2f}"
    
    def __calculate_price(self) -> float:
        # This method is private and not accessible outside this class
        return self.__price
    
    def get_price(self) -> float:
        # Public method to access the price
        return self.__calculate_price()
    
    # Private method to simulate brewing the coffee
    def __brew(self) -> str:
        return f"Brewing {self.size} {self.drink_type} for {self.customer_name}."
    
    def make_coffee(self) -> str:
        # Public method to make coffee
        return self.__brew()
    
drink = CoffeOrder("John Doe", "Latte", "Medium")
print(drink.get_order_summary())  # Output: Order for John Doe: Medium Latte - $5.00
print(drink.get_price())  # Output: 5.0
print(drink.make_coffee())  # Output: Brewing Medium Latte for John Doe.