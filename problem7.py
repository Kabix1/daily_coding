#!/usr/bin/env python

FIB_SAVED = [1, 1]


def fib(n: int) -> int:
    if len(FIB_SAVED) > n:
        return FIB_SAVED[n]
    else:
        return fib(n - 1) + fib(n - 2)


def decode_permutations(message: str) -> int:
    breakpoints = [0]
    permutations = 1
    for i in range(len(message) - 1):
        char = message[i:i + 2]
        if char[0] == "0":
            breakpoints.append(i + 1)
        elif char[1] == "0":
            breakpoints.append(i)
            breakpoints.append(i + 1)
        elif int(char) > 26:
            breakpoints.append(i + 1)
    for i in range(len(breakpoints) - 1):
        permutations *= fib(breakpoints[i + 1] - breakpoints[i])
    permutations *= fib(len(message) - breakpoints[-1])
    print(message)
    return permutations


if __name__ == "__main__":
    print(decode_permutations("22222"))
    print(decode_permutations("22022"))
    print(decode_permutations("22622"))
    print(decode_permutations("22922"))
    print(decode_permutations("26622"))
    print(decode_permutations("2269102922"))
