class InputManager:
    def __init__(self):
        self.numbers = []

    def add_number(self, value):
        self.numbers.append(value)

    def find_index(self, target):
        if target in self.numbers:
            return self.numbers.index(target) + 1
        return -1


def main():
    manager = InputManager()

    # Input N
    n = int(input("Plz enter a positive integer N: "))
    if n <= 0:
        print("Plz enter a positive integer.")
        return

    # Input N numbers
    for i in range(n):
        num = int(input(f"Enter number {i + 1} of {n}: "))
        manager.add_number(num)

    # Input X
    x = int(input("Enter the integer X to search for: "))

    # Output
    print(manager.find_index(x))


if __name__ == "__main__":
    main()