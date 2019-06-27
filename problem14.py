#!/usr/bin/env python
###############################################################################
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# The area of a circle is defined as πr^2. Estimate π to 3 decimal places
# using a Monte Carlo method.
#
# Hint: The basic equation of a circle is x2 + y2 = r2.
###############################################################################

import random


def calc_pi():
    inside, total = 0, 0
    for _ in range(10000000):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside += 1
        total += 1
    print(inside / total * 4)


if __name__ == "__main__":
    calc_pi()
