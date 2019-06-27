#!/usr/bin/env python
########################################################################
# Given a stream of elements too large to store in memory, pick a random
# element from the stream with uniform probability.
########################################################################

import random


def rand_from_stream(stream):
    num, val = 0, 0
    for n in stream:
        rand = random.random()
        if rand > val:
            num = n
            val = rand
    print(num)


def reservoir_sample(population, sample_size):
    sample = []
    for i, n in enumerate(population):
        if i < sample_size:
            sample.append(n)
        else:
            j = random.randint(0, i + 1)
            if j < sample_size:
                sample[j] = n
    return sample


if __name__ == "__main__":
    rand_from_stream([2, 4, 5, 6, 7, 3, 5])
    print(reservoir_sample([2, 4, 5, 6, 7, 3, 5], 2))
