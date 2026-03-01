"""
The program asks the user for input N (positive integer) and reads it.

Then the program asks the user for input k (positive integer) and reads it.

Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.

In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

Additionally, provide the variance of labels in the training dataset.

The basic functionality of data processing (data initialization, data insertion), should be done using Numpy library while the computation (ML) part should be done using Scikit-learn library as much as possible (note: you can combine with what you've done from the previous task).
"""


import numpy as np
def data_input():
    try:
        N = int(input("input a number n: "))
        k = int(input("input a number k: "))

        if k > N:
            print("exception when input")
            return
        x_coords = []
        y_coords = []

        # Input N points
        for i in range(N):
            s = input(f"input point {i+1} in format (x,y)")
            x, y = map(float, s.split(","))
            x_coords.append(x)
            y_coords.append(y)

        return x_coords, y_coords, k
    except ValueError:
        print("exception when input")
        return

from sklearn.neighbors import KNeighborsRegressor
def main():
    data = data_input()
    if data is None:
        return
    xs, ys, k = data

    xs = np.array(xs).reshape(-1, 1)
    ys = np.array(ys)
    knn_regressor = KNeighborsRegressor(n_neighbors=k)
    knn_regressor.fit(xs, ys)
    print("variance of label", np.var(ys))

    try:
        x = float(input(f"input a point x"))
    except ValueError:
        print("exception when input")
        return
    y = knn_regressor.predict(np.array([[x]], dtype=float))[0]
    print("res: ", float(y))


if __name__ == "__main__":
    main()
"""
output:

input a number n: 5
input a number k: 2
input point 1 in format (x,y)1,2
input point 2 in format (x,y)2,3
input point 3 in format (x,y)3,4
input point 4 in format (x,y)4,5
input point 5 in format (x,y)5,6
variance of label 2.0
input a point x2
res:  2.5

Process finished with exit code 0
"""