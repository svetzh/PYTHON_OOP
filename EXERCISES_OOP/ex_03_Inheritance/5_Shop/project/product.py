<<<<<<< HEAD
class Product:
    def __init__(self, name: str, quantity: int):
        self.quantity = quantity
        self.name = name

    def increase(self, quantity):
        self.quantity += quantity

    def decrease(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity

    def __repr__(self):
        return self.name
=======
class Product:
    def __init__(self, name: str, quantity: int):
        self.quantity = quantity
        self.name = name

    def increase(self, quantity):
        self.quantity += quantity

    def decrease(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity

    def __repr__(self):
        return self.name
>>>>>>> 276765b8e88ecb03013f4fe22c25ddcd3699ae0d
