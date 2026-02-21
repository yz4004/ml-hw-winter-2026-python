from typing import List

import numpy as np


class KNNRegression:
    """
    knn regression
    take k-closet points in x-coordinates, then average on their y

    """
    def __init__(self, k, x_values: np.array, y_values: np.array):
        self.k = k
        self.data = np.column_stack((x_values, y_values)) # vertical stacked [(x1,y1), (x2,y2)...]

    def predict(self, x_query):

        # k closest point in x-direction
        distances = np.abs(self.data[:, 0] - x_query)
        k_indices = np.argsort(distances)[:self.k]

        # average on y
        prediction = np.mean(self.data[k_indices, 1])
        return prediction


def main():
    try:
        N = int(input("Enter the number of points (N): "))
        k = int(input("Enter the number of neighbors (k<=N): "))


        x_coords = []
        y_coords = []

        # Input N points
        print(f"Please provide {N} points:")
        for i in range(N):
            x = float(input(f" Point {i + 1} x: "))
            y = float(input(f" Point {i + 1} y: "))
            x_coords.append(x)
            y_coords.append(y)

        knn = KNNRegression(k, np.array(x_coords), np.array(y_coords))

        x_query = float(input("Enter the X value to predict Y: "))

        result = knn.predict(x_query)
        print(f"The predicted Y value is: {result}")

    except ValueError:
        print("Error: Please ensure you enter valid numbers.")


if __name__ == "__main__":
    main()

"""
sample: output: 


Enter the number of points (N): 5
Enter the number of neighbors (k<=N): 2
Please provide 5 points:
Point 1 x: 2
Point 1 y: 3
Point 2 x: 4
Point 2 y: 5.3
Point 3 x: 7.25
Point 3 y: 456
Point 4 x: 4564
Point 4 y: 787
Point 5 x: 484
Point 5 y: 55
Enter the X value to predict Y: 5
The predicted Y value is: 230.65
"""