# module5_call.py
from module5_mod import InputManager


def run():
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
    run()