from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    res = [0 for i in range(len(A))]
    carry = 0
    for i in reversed(range(0, len(A))):
        currRes = 0
        num = A[i]
        if i == len(A) - 1 or carry > 0: # for the last number or if there is a carry
            currRes = num + 1
        else: # for all other numbers
            currRes = num

        if currRes >= 10:
            carry += 1
        else:
            carry = 0
        res[i] = currRes % 10
    return [1] + res if carry > 0 else res

#solution
# def plus_one(A: List[int]) -> List[int]:
#     A[-1] += 1
#     for i in reversed(range(1, len(A))):
#         if A[i] != 10:
#             break
#         A[i] = 0
#         A[i - 1] += 1
#     else:
#         if A[0] == 10:
#             # There is a carry-out, so we need one more digit to store the result.
#             # A slick way to do this is to append a 0 at the end of the array,
#             # and update the first entry to 1.
#             A[0] = 1
#             A.append(0)
#     return A

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
