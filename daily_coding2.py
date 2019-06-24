#!/usr/bin/env python

a = [1, 2, 3, 4, 5]

prod = 1
for n in a:
    prod *= n
b = [int(prod/n) for n in a]
print(b)

b = [1]*len(a)
for i in range(len(b)):
    for j, n in enumerate(a):
        if i != j:
            b[i] *= n
print(b)
