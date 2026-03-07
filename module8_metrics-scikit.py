"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X is treated as the ground truth (correct) class label and Y is treated as the predicted class. Both X and Y are either 0 or 1.

In the end, the program outputs: the Precision and Recall based on the inputs.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous tasks).
"""

import numpy as np
from sklearn.metrics import precision_score, recall_score


def data_input():
    try:
        N = int(input("input a number n: "))

        x_coords = []
        y_coords = []

        for i in range(N):
            s = input(f"input point {i+1} in format (x,y)")
            x, y = map(int, s.split(","))

            if x not in (0, 1) or y not in (0, 1):
                print("invalid input, should be 0/1")
                return

            x_coords.append(x)
            y_coords.append(y)

        return x_coords, y_coords

    except ValueError:
        print("exception when input")
        return


def main():
    data = data_input()
    if data is None:
        return

    xs, ys = data

    xs = np.array(xs)
    ys = np.array(ys)

    precision = precision_score(xs, ys, zero_division=0)
    recall = recall_score(xs, ys, zero_division=0)

    print("precision", float(precision))
    print("recall", float(recall))


if __name__ == "__main__":
    main()

"""
local test result:
input a number n: 4
input point 1 in format (x,y)1,1
input point 2 in format (x,y)1,0
input point 3 in format (x,y)0,1
input point 4 in format (x,y)0,0
precision 0.5
recall 0.5

Process finished with exit code 0

"""