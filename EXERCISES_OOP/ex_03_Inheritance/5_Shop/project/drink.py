<<<<<<< HEAD
from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.QUANTITY)  # -> self.QUANTITY is the same

=======
from project.product import Product


class Drink(Product):
    QUANTITY = 10

    def __init__(self, name):
        super().__init__(name, self.QUANTITY)  # -> self.QUANTITY is the same

>>>>>>> 276765b8e88ecb03013f4fe22c25ddcd3699ae0d
