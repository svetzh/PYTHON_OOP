class StrMixin:
    str_delimiter = ", "  # this is some kind a state that is not very  crucial to the logic

    def __str__(self):
        return self.str_delimiter.join(f"{key}={value}" for key, value in self.__dict__.items())


class Person(StrMixin):
    def __init__(self, name, age):
        self.age = age
        self.name = name


class Building(StrMixin):
    str_delimiter = ";"

    def __init__(self, name, address):
        self.name = name
        self.address = address


print(Person("Svet", 39))
print(Building("Softuni", "Александър Малинов №78"))