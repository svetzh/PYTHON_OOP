# MRO
class Parent:
    def a(self):
        return "parent"


class FirstChild(Parent):
    pass
    def a(self):
        return "1c"

class SecondChild(Parent):
    pass
    def a(self):
        return "2c"

class GrandChild(SecondChild, FirstChild):
    pass
    def a(self):
        return "gc"


gc = GrandChild()
print(GrandChild.mro())
print(gc.a())