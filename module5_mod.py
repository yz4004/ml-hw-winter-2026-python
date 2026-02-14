class InputManager:
    def __init__(self):
        self.numbers = []

    def add_number(self, value):
        self.numbers.append(value)

    def find_index(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1
        return -1
