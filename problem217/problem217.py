#!/usr/bin/env python

import time
from timer import time_func, end_timers
import timer
import numpy as np
import time_functions
import matplotlib.pyplot as plt
import math

# import memory_profiler
from memory_profiler import profile

# @profile
scale = 10**(10**4)


def get_file_input(filename: str):
    with open(filename) as f:
        content = f.readlines()
    numbers = [int(x.strip()) for x in content]
    return numbers


def main():
    max, num = scale, 10**2
    sample = get_file_input("input.txt")
    time_functions.plot_times(
        [next_sparse_string, next_sparse_bit, next_sparse_louis],
        # time_functions.plot_times([next_sparse_string, log],
        sample,
        file_name="problem217_log.data",
        repeats=1,
        n_tests=10**4)

    # data = np.loadtxt("problem217.data")
    # x = data[0, :]
    # values = data[1:, :]
    # fig, ax = plt.subplots()
    # for y in values:
    #     v = [10**val for val in y]
    #     ax.plot(x, v)

    # ax.set_xlabel('Input')
    # ax.set_ylabel('Time [s]')
    plt.show()

    # max = 10**3
    # for n in timer.get_lin_sample(1, max, num):
    #     s_sol = next_sparse_string(n)
    #     b_sol = next_sparse_bit(n)
    #     l_sol = next_sparse_louis(n)
    #     s = bin(n).split('b')[1]
    #     print(
    #         f"{n} ({s}): {s_sol} ({bin(s_sol)}), {b_sol} ({bin(b_sol)}), {l_sol} ({bin(l_sol)})"
    #     )
    # print(end_timers())


def linear(n: int):
    time.sleep(n / scale)


# @timer.log
def log(n: int):
    # time.sleep(0.01)
    time.sleep(math.log10(n)**2 / (math.log10(scale)**2 / 0.01))
    # time.sleep(math.log10(n + 1) / scale)


# @time_func
# @profile
# @timer.log
def next_sparse_string(n: int):
    s = bin(n).split('b')[1]
    if is_sparse(s):
        return n
    parts = s.split('11', 1)
    body = parts[0]
    if "00" in body:
        rev = body[-1::-1]
        body_parts = rev.split("00", 1)
        head = body_parts[1][-1::-1] + "01"
        tail = "0" * (len(parts[1]) + 2 + len(body_parts[0]))
    else:
        head = "1" + "0" * len(body)
        tail = "0" * (len(parts[1]) + 2)
    return int(head + tail, 2)


def next_sparse_louis(x):
    bin = []
    while (x != 0):
        bin.append(x & 1)
        x >>= 1
    bin.append(0)
    n = len(bin)
    last_final = 0
    for i in range(1, n - 1):
        if ((bin[i] == 1 and bin[i - 1] == 1 and bin[i + 1] != 1)):
            bin[i + 1] = 1
            for j in range(i, last_final - 1, -1):
                bin[j] = 0
                last_final = i + 1
    ans = 0
    for i in range(n):
        ans += bin[i] * (i << i)
    return ans
    print(bin)


# @time_func
# @profile
# @timer.log
def next_sparse_bit(n: int):
    zero_count, one_count, last_one, first_zero, i = 0, 0, 0, 0, 0
    first_zero_index = 0
    bit = 1
    while n >= bit:
        if n & bit:
            one_count += 1
            zero_count = 0
        else:
            one_count = 0
            zero_count += 1
        if one_count >= 2:
            last_one = bit
            first_zero = 0
        if zero_count >= 2 and last_one and not first_zero:
            first_zero = bit >> 1
            first_zero_index = i
        bit <<= 1
        i += 1
    if not last_one:
        return n
    if not first_zero:
        return bit
    else:
        return (n >> first_zero_index << first_zero_index) + first_zero


def is_sparse(s):
    clusters = get_clusters(s)
    if clusters:
        return False
    return True


def get_clusters(s):
    ones = s.split("0")
    return [cluster for cluster in ones if len(cluster) >= 2]


def generate_numbers():
    sample = np.random.randint(1, 2**30, 100)
    for n in sample:
        print(n)


if __name__ == "__main__":
    # generate_numbers()
    main()
