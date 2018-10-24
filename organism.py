import math
import random


class Organism:

    def activation(self, x):
        return 1. / (1. + math.exp(-x))

    def __init__(self, alpha=random.random()):
        self.alpha = alpha

    def predict(self, x):
        return self.activation(x * self.alpha)

    def mutate(self):
        self.alpha = random.random()