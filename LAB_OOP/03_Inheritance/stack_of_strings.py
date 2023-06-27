class Stack:
    def __init__(self):
        self.element = None
        self.data = []

    def push(self, element):
        if not isinstance(element, str):
            raise TypeError("Only strings can be appended to the Stack")
        return self.data.append(element)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        return None

    def top(self):
        if not self.is_empty():
            return self.data[-1]
        return None

    def is_empty(self):
        # if not self.data:
        #     return False
        # return True
        return len(self.data) == 0

    def __str__(self):
        elements = ", ".join(self.data[::-1])
        return f"[{elements}]"


