import sys
from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    can_reach = 0
    for i in range(0, len(A)):
        if i <= can_reach:
            can_reach = max(can_reach, A[i] + i)
    return can_reach >= len(A) - 1


# def can_reach_end_helper(A: List[int], currIdx: int, memo: List[int]) -> bool:
#     # print("currIdx: ", currIdx)
#     if memo[currIdx] != -1:
#         return memo[currIdx]
#
#     maxStep = A[currIdx]
#     # print("maxStep: ", maxStep)
#
#     if currIdx >= len(A) - 1:
#         return True
#
#     if currIdx < len(A) - 1 and maxStep == 0:
#         return False
#
#     for i in range(1, maxStep+1):
#         canReachEndFromCurrIdx = can_reach_end_helper(A, currIdx + i, memo)
#         if (canReachEndFromCurrIdx):
#             memo[currIdx] = True
#             return True
#
#     memo[currIdx] = False
#     return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
