#!/usr/bin/env python


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def first(a, b):
        return a
    return pair(first)

def cdr(pair):
    def second(a, b):
        return b
    return pair(second)

if __name__ == "__main__":
    pair = cons(3, 4)
    print(car(pair))
    print(cdr(pair))

