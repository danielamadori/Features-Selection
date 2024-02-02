import numpy as np

def checkMetrics(metrics, allowedMetrics):
    if not isinstance(metrics, list):  # Check if the metrics is a list
        metrics = [metrics]

    if not set(metrics).issubset(allowedMetrics):  # check if the metrics are valid
        raise ValueError('Invalid metrics function')

    return list(dict.fromkeys(metrics))  # Remove duplicates without changing the order


def createFeatureScore(metrics, positiveValue=False):
    score = dict()
    value = -np.Inf
    if positiveValue:
        value = -value

    for metric in metrics:
        score[metric] = value

    return score


# Return True if score1 is better than score2 considering all the metrics with order of priority, False otherwise
def compareFeatureScore(score1, score2, metrics):
    for metric in metrics:
        if score1[metric] > score2[metric]:
            return True
        if score1[metric] < score2[metric]:
            return False
        # If the two scores are equal, continue to the next metric

    return False  # If all the metrics are equal, return False
