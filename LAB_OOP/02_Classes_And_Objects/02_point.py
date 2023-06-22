class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self):
        pass

    def set_y(self):
        pass


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)