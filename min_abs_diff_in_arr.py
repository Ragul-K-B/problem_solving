"""
You have an array of integers.
Your task is to find the smallest absolute difference between
any two numbers in that array. The absolute difference is the
positive difference between two numbers. You need to check all possible pairs
of numbers in the array and return the smallest difference you find.
"""


def minimumAbsoluteDifference(arr):
    arr.sort()

    min_diff = float('inf')

    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        if diff < min_diff:
            min_diff = diff

    return min_diff