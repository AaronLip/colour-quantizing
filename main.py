from PIL import Image
from decimal import Decimal
import random
import math
import os

class Cluster(object):
    """Store the rolling centroid of a cluster of samples."""

    def __init__(self, *centroid):
        self.sample_size = 0
        if centroid:
            self.new_sample(*centroid)

    def new_sample(self, *values):
        """Update a cluster's centroid when a new sample is added to it."""
        if self.sample_size == 0:
            self.centroid = [Decimal(v) for v in values]
        else:
            self.centroid = [self.centroid[i] + (Decimal(values[i]) - self.centroid[i]) / (self.sample_size + 1) for i in range(len(values))]
        self.sample_size += 1

def kmeans(data, k=3, max_iterations=5):
    """Initialize k clusters with semi-random centroids and begin assigning pixels to their nearest centroid until the iteration maximum is hit."""
    clusters = [Cluster(*random.choice(data)) for _ in range(k)]

    iterations = 0
    while iterations < max_iterations:

        print(f'Iteration #{iterations}')

        for i, pixel in enumerate(data):
            nearest = min(clusters, key=lambda cluster: math.sqrt(sum((a - b) ** 2 for a, b in zip(cluster.centroid, pixel))))
            nearest.new_sample(*pixel)

        iterations += 1

    return [c.centroid for c in clusters]

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 2:
        print(kmeans(Image.open(sys.argv[1]).getdata(), int(sys.argv[2])))