#!/usr/bin/env python

import time
import math
import numpy as np

timers = {}
start = 0

log_counter = {}


def log(func):
    def logged(*argc, **kwargs):
        # log_counter.getdefault(func.__name__)
        log_counter[func.__name__] = log_counter.get(func.__name__, 0) + 1
        print(
            f"Before function {func.__name__} num: {log_counter[func.__name__]}"
        )
        ret = func(*argc, **kwargs)
        # print(f"After function {func.__name__}")
        return ret

    return logged


def log_arg(func):
    def logged(*argc, **kwargs):
        print(f"Before function {func.__name__} with args {argc}")
        ret = func(*argc, **kwargs)
        # print(f"After function {func.__name__}")
        return ret

    return logged


def time_func(func):
    def timed(*args, **kwargs):
        global start, timers
        t0 = time.time()
        if not start:
            start = t0
        ret = func(*args, **kwargs)
        t1 = time.time()
        timers.setdefault(func.__name__, []).append(t1 - t0)
        # timers[func.__name__] = timers.setdefault(func.__name__,
        # []).append(t1 - t0)
        return ret

    return timed


def end_timers():
    global start, timers
    total = time.time() - start
    start = 0
    timers = dict(timers)
    result = {}
    for func, data in timers.items():
        result[func] = sum(data)
    result["Total"] = total
    return result


def get_lin_sample(start, stop, num):
    start, stop = int(start), int(stop)
    step_size = (stop - start) // num + 1
    current = start
    sample = []
    while current <= stop:
        sample.append(current)
        current += step_size
    return sample


def get_log_sample(start, stop, num):
    print("Generating sample")
    log_start = math.log10(start)
    log_stop = math.log10(stop)
    # lin_sample = get_lin_sample(log_start, log_stop, num)
    lin_sample = np.linspace(log_start, log_stop, num)
    # return lin_sample
    log_sample = [10**int(n) for n in lin_sample]
    return log_sample
