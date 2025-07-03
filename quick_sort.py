"""Function structure for sorting through Quick Sort"""

import time


def sorter_2(array):
    """Quick Sort Function"""
    start_time = time.time()

    if len(array) <= 1:
        stop_time = time.time()

        mil_elapsed_time = (stop_time - start_time)*1000
        return array, mil_elapsed_time
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        right = [x for x in array[1:] if x >= pivot]

        sorted_left, _ = sorter_2(left)
        sorted_right, _ = sorter_2(right)

        stop_time = time.time()
        mil_elapsed_time = (stop_time - start_time)*1000

        sorted_list = sorted_left + [pivot]+sorted_right

        return sorted_list, mil_elapsed_time
