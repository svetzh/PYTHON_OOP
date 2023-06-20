# def print_list(list_arg):
#     for el in list_arg:
#         if el is not None:
#             print(el)
#
#
# list1 = [1, 2, 3]
# print_list(list1)
#
# list2 = [3, 4, 5]
# print_list(list2)


class Person:
    def __init__(self, name):
        self.name = name


person1 = Person("Ivona")
person2 = Person("Diyan")

print(person1.name)