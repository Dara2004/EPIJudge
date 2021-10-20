import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
# and mutate the array
# [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6]
def delete_duplicates(A: List[int]) -> int:
    write_idx = 1 #the next dup number to be replaced
    for i in range(1, len(A)):
        if A[i] != A[write_idx-1]: #found a new number that we currently don't have (write_idx-1 represents the last num we have)
            A[write_idx] = A[i]
            write_idx += 1
    return write_idx


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
