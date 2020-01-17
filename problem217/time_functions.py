import pandas as pd
from functools import partial
import timeit
import timer
import numpy as np
import math
import matplotlib.pyplot as plt
import yaml


# @timer.log
def plot_times(functions, inputs, repeats=3, n_tests=1, file_name=""):
    timings = get_timings(functions, inputs, repeats=repeats, n_tests=n_tests)
    results = aggregate_results(timings)
    if file_name:
        data = []
        data.append(results.index)
        for func in results.columns.levels[0]:
            data.append(results[func, 'avg'])
            np.savetxt(file_name, data)
    fig, ax = plot_results(results)
    return fig, ax, results


# @timer.log
def get_timings(functions, inputs, repeats, n_tests):
    for func in functions:
        result = pd.DataFrame(index=[i for i in inputs],
                              columns=range(repeats),
                              data=(timeit.Timer(partial(func, i)).repeat(
                                  repeat=repeats, number=n_tests)
                                    for i in inputs))
        yield func, result


# @timer.log
def aggregate_results(timings):
    empty_multiindex = pd.MultiIndex(levels=[[], []],
                                     labels=[[], []],
                                     names=['func', 'result'])
    aggregated_results = pd.DataFrame(columns=empty_multiindex)

    for func, timing in timings:
        for measurement in timing:
            aggregated_results[func.
                               __name__, measurement] = timing[measurement]
        aggregated_results[func.__name__, 'avg'] = timing.mean(axis=1)
        aggregated_results[func.__name__, 'yerr'] = timing.std(axis=1)

    return aggregated_results


@timer.log
def plot_results(results):
    fig, ax = plt.subplots()
    x = results.index
    for func in results.columns.levels[0]:
        y = results[func, 'avg']
        yerr = results[func, 'yerr']
        ax.errorbar(x, y, yerr=yerr, fmt='-o', label=func)

    ax.set_xlabel('Input')
    ax.set_ylabel('Time [s]')
    ax.legend()
    return fig, ax
