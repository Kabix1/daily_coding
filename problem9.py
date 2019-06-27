#!/usr/bin/env python
import random


def biggest_sum(numbers: list) -> int:
    """Calculate the biggest sum from non-adjacent numbers"""
    running = [0, 0]
    current = 0
    for n in numbers:
        running[current] = max(running[current] + n, running[1 - current])
        current = 1 - current
    return max(running)


if __name__ == "__main__":
    seq = [random.randint(1, 9) for i in range(10)]
    print(f"seq: {seq}, res: {biggest_sum(seq)}")
    biggest_sum([2, 4])
