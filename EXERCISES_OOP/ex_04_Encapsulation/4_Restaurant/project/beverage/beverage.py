from project.product import Product

class Beverage(Product):
    def __init__(self, name: str, price: float, milliliters: float):
        super().__init__(name, price)  # inherit it
        self.__milliliters = milliliters  # extend the functionality of Product

    @property
    def milliliters(self):
        return self.__milliliters


