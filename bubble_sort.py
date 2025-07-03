"""Function structure for sorting through Bubble Sort"""
import time


def sorter_1(array):
    """Bubble Sorting Function"""
    start_time = time.time()

    for y in range(len(array) - 1, 0, -1):
        for x in range(y):
            if array[x] > array[x+1]:
                array[x], array[x+1] = array[x+1], array[x]
    stop_time = time.time()
    mil_elapsed_time = (stop_time - start_time)*1000
    return array, mil_elapsed_time
