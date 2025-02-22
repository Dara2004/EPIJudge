import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

### first solution ###
# Time: O(2N), space: O(1)
# def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
#     smaller, pivot, larger = 0, A[pivot_index], len(A) - 1
#     for i in range(0, len(A)):
#         if A[i] < pivot:
#             A[i], A[smaller] = A[smaller], A[i] #swap array elements
#             smaller += 1
#     for i in reversed(range(0, len(A))):
#         if A[i] > pivot:
#             A[i], A[larger] = A[larger], A[i]
#             larger -= 1

### optimal solution ###
# Time: O(N), space: O(1)
def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    # think of partitioning the array into 3 parts: smaller, unclassified, larger
    s, e, l, pivot = 0, 0, len(A) - 1, A[pivot_index] #smaller, equal, larger
    while e <= l:
        # A[e] = the next unclassified number to be classified
        if A[e] < pivot: # about to classify number as smaller
            A[e], A[s] = A[s], A[e]
            e += 1 # move e to the next unclassified number
            s += 1 # move s to the next smaller number
        elif A[e] == pivot: #curr number at e is about to be classified as smaller
            e += 1
        else: #curr number at e is about to be classified as smaller
            A[e], A[l] = A[l], A[e]
            l -= 1 # move l to the next larger number

@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
