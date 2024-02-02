import numpy as np

# P(c) the probability of each value
def probability(X):
    _, counts = np.unique(X, return_counts=True)
    return counts / len(X)

# P(X|Y) the probability of each value given the input
def jointProbabilities(X, Y):
    unique_x, counts_x = np.unique(X, return_counts=True)
    unique_y, counts_y = np.unique(Y, return_counts=True)

    joint_probabilities = np.zeros((len(unique_x), len(unique_y)))
    for i, x in enumerate(unique_x):
        for j, y in enumerate(unique_y):
            joint_probabilities[i, j] = np.mean(np.logical_and(X == x, Y == y))

    return joint_probabilities
