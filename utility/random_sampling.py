import random

# Weighted Random Sampling without Replacement
# Taken from https://maxhalford.github.io/blog/weighted-sampling-without-replacement/
# A method by Efraimidis and Spirakis (2006). https://doi.org/10.1016/j.ipl.2005.11.003
# Time complexity: O(N * log N)
def weighted_sample_without_replacement(population, weights, k, rng=random):
    v = [rng.random() ** (1 / w) for w in weights]
    order = sorted(range(len(population)), key=lambda i: v[i])
    return [population[i] for i in order[-k:]]
