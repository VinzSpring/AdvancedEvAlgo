import math
import random

from organism import Organism
from matplotlib import pyplot as plt

min_errors = []


def get_error(x, y):
    return math.fabs(y - x)


def get_best_organism(organisms, x, y):
    errors = []
    for o in organisms:
        errors.append(
            get_error(o.predict(x), y)
        )
    min_errors.append(min(errors))
    return organisms[errors.index(min(errors))]


def merge_organisms(organisms):
    alphas = [o.alpha for o in organisms]
    return Organism(
        alpha=sum(alphas) / len(alphas)
    )


def lin_func(x):
    hidden_aplha = .732
    return 1. / (1. + math.exp(-(hidden_aplha * x)))


if __name__ == "__main__":
    population = [
        [Organism(), Organism(), Organism()],
        [Organism(), Organism(), Organism()],
        [Organism(), Organism(), Organism()],
    ]

    for i_generation in range(1000):

        best_organisms = []
        xs = []
        for tribe in population:
            x = random.random()
            xs.append(x)
            y = lin_func(x)
            best_organisms.append(get_best_organism(tribe, x, y))

        crossbred_child = merge_organisms(best_organisms)
        errors = [
            get_error(best_organisms[i].predict(xs[i]), lin_func(xs[i])) for i in range(len(xs))
        ]
        i = errors.index(max(errors))
        j = population[i].index(best_organisms[i])

        for tribe in population:
            for o in tribe:
                if o in best_organisms:
                    continue
                else:
                    o.mutate()

        population[i][j] = crossbred_child

    plt.plot(min_errors)
    plt.show()
