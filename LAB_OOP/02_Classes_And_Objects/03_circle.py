class Circle:
    pi = 3.14  # DEMO always use math.pi ("pi" is class attribute)

    def __init__(self, radius: float):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        area = (self.radius * self.radius) * self.pi  # access class attribute with 'self'
        return area

    def get_circumference(self):
        circ = 2 * self.pi * self.radius
        return circ


circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
