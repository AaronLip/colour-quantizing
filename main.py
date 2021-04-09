from PIL import Image
from decimal import Decimal
import random
import math
import os
import itertools

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
            nearest = min(clusters, key=lambda cluster: euclidean_distance(cluster.centroid, pixel))
            nearest.new_sample(*pixel)

        iterations += 1

    return [c.centroid for c in clusters]

def euclidean_distance(origin, point):
    """Calculate the distance between a point and a point of origin."""
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(origin, point)))

def quantize_image(image, centroids):
    for x, y in itertools.product(range(image.size[0]), range(image.size[1])):
        image.putpixel((x, y), tuple(int(i) for i in min(centroids, key=lambda centroid: euclidean_distance(centroid, image.getpixel((x, y))))))
    image.show()

if __name__ == '__main__':
    import sys

    if len(sys.argv) > 2:
        with Image.open(sys.argv[1]) as image:
            centroids = kmeans(image.getdata(), int(sys.argv[2]))
            quantize_image(image, centroids)