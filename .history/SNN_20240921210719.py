import pandas as pd
import numpy as np
from sklearn.neighbors import BallTree
import statistics

class SNN:
    def __init__(self, metric='euclidian'):
        self.metric = metric

    def get_pairwise_distances(self, data, k):
        data = pd.DataFrame(data)
        balltree = BallTree(data, metric=self.metric)
        knn = balltree.query(data, k=k+1)[1]
        pairwise_distances = np.zeros((len(data), len(data)))
        for i in range(len(data)):
            for j in range(i+1, len(data)):
                if (j in knn[i]) and (i in knn[j]):
                    weight = len(set(knn[i]).intersection(set(knn[j])))
                    pairwise_distances[i][j] = weight
                    pairwise_distances[j][i] = weight
        return pairwise_distances

    def fit_predict(self, data, k):
        data = pd.DataFrame(data)
        pairwise_distances = self.get_pairwise_distances(data, k)
        scores = [statistics.mean(sorted(x, reverse=True)[:k]) for x in pairwise_distances]
        min_score = min(scores)
        max_score = max(scores)
        scores = [min_score + (max_score - x) for x in scores]
        return scores
