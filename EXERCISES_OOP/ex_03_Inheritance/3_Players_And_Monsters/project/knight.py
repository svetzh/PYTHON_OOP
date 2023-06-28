<<<<<<< HEAD
from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    # def __str__(self):
=======
from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level):
        super().__init__(username, level)

    # def __str__(self):
>>>>>>> 276765b8e88ecb03013f4fe22c25ddcd3699ae0d
    #     return f"{self.username} of type {self.__class__.__name__} has level {self.level}"