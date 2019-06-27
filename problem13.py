#!/usr/bin/env python

##############################################################################
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest
# substring that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".
###############################################################################


def longest_substring(s: str, k: int) -> str:
    candidates = []
    longest = []
    for c in s:
        if not candidates or not candidates[-1][-1] == c:
            candidates.append([])
        candidates = [
            cand for cand in candidates if c in cand or len(set(cand)) < k
        ]
        for cand in candidates:
            cand.append(c)
            if len(cand) > len(longest):
                longest = list(cand)
    print(longest)


if __name__ == "__main__":
    longest_substring("abcbfabat", 3)
