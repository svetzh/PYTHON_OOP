from functools import reduce

class Calculator:

    @staticmethod
    def add(*args):
        # result = 0
        # for num in args:
        #     result += num
        # return result
        return reduce(lambda x, y: x+y, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda x, y: x-y, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda x, y: x/y, args)

    @staticmethod
    def multiply(*args):
        # result = 1
        # for num in args:
        #     result *= num
        # return result
        return reduce(lambda x, y: x*y, args)


a = Calculator.add(5, 6, 4)
print(a)

m = Calculator.multiply(3, 10, 2)
print(m)

d = Calculator.divide(81, 9)
print(d)

s = Calculator.subtract(10, 4, 5, 2)
print(s)