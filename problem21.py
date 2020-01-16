##################################################################
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
########################################################################

#!/usr/bin/env python


def num_rooms(lectures):
    activity = []
    for lecture in lectures:
        start, end = lecture[0], lecture[1]
        if end >= len(activity):
            activity.extend([0 for i in range(end + 1 - len(activity))])
        for i in range(start, end + 1):
            activity[i] += 1
    return max(activity)


if __name__ == "__main__":
    print(num_rooms([(30, 75), (0, 80), (60, 150), (75, 100)]))
