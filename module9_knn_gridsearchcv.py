import numpy as np
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier


def readData(size, dataset_name):
    x_values = np.empty((size, 1), dtype=float)
    y_values = np.empty(size, dtype=int)

    print(f"give {size} (x, y) for {dataset_name}:")
    for i in range(size):
        x_values[i, 0] = float(input(f"{dataset_name} pair {i + 1} x: "))
        y_values[i] = int(input(f"{dataset_name} pair {i + 1} y:"))

    return x_values, y_values



def filter_valid_k_values(candidate_k, x_train, y_train, cv_strategy):
    valid_k = []
    for k in candidate_k:
        is_valid = True
        for train_index, _ in cv_strategy.split(x_train, y_train):
            if k > len(train_index):
                is_valid = False
                break
        if is_valid:
            valid_k.append(k)
    return valid_k


def main():
    try:

        n = int(input("input a number n: "))
        x_train, y_train = readData(n, "TrainS")

        m = int(input("input a number m: "))

        x_test, y_test = readData(m, "TestS")
    except Exception:
        return 0

    candidate_k = list(range(1, n + 1))

    n_samples = len(y_train)
    n_splits = min(5, n_samples)
    kfold = KFold(n_splits=n_splits)


    candidate_k = filter_valid_k_values(candidate_k, x_train, y_train, kfold)
    grid_search = GridSearchCV(
        estimator=KNeighborsClassifier(),
        param_grid={"n_neighbors": candidate_k},
        scoring="accuracy",
        cv=kfold
    )
    grid_search.fit(x_train, y_train)
    best_k = grid_search.best_params_["n_neighbors"]
    best_model = grid_search.best_estimator_

    y_pred = best_model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("best k", int(best_k))
    print("test accuracy", float(accuracy))


if __name__ == "__main__":
    main()
