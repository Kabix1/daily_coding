#!/usr/bin/env python
##############################################################################
# You run an e-commerce website and want to record the
# last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# record(order_id): adds the order_id to the log
# get_last(i): gets the i:th last element from the log. i is guaranteed to be
# smaller than or equal to N.
# You should be as efficient with time and space as possible.


class OrderLog:
    def __init__(self, N):
        self.N = N
        self.orders = []

    def record(self, order_id):
        if len(self.orders) >= self.N:
            self.orders.pop(0)
        self.orders.append(order_id)

    def get_last(self, i):
        return self.orders[-i]


if __name__ == "__main__":
    log = OrderLog(20)
    log.record("12345")
    log.record("32345")
    log.record("42345")
    log.record("16345")
    print(log.get_last(2))
