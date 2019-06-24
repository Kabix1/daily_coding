#!/usr/bin/env python


def find_lowest_missing(numbers):
    tot = sum(numbers)
    high = max(numbers)
    length = len(numbers)
    avg = tot/length
    avg2 = (high+1)/2
    temp = [n-avg2 for n in numbers]
    print(temp)
    print(sum(temp))
    print(sum([abs(n) for n in temp]))
    # print([n-])
    # if high == length:
    #     return high + 1

if __name__ == "__main__":
    # find_lowest_missing([1,2,3,4,5])
    find_lowest_missing([6,2,3,1,5,10])
