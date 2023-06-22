class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.calc_space_left() <= self.content + ml:
            return f"Cannot add {ml} ml"
        else:
            self.content += ml
            return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.calc_space_left()} ml left"

    def calc_space_left(self):
        return self.capacity - self.content


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())