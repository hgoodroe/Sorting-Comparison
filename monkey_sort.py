"""Function structure for sorting through random methods aka Monkey Sort"""

import time
import random


def sorter_3(array):
    """Sorter that houses Random / Monkey Sort"""

    start_time = time.time()

    def monkey_system(array):

        while True:

            rand_num_1 = random.randint(0, (len(array)-1))
            rand_num_2 = random.randint(0, (len(array)-1))

            if rand_num_1 > rand_num_2:
                array[rand_num_1], array[rand_num_2] = array[rand_num_2], array[rand_num_1]

            if array == sorted(array):
                break

        return array

    array = monkey_system(array)
    stop_time = time.time()
    mil_elapsed_time = (stop_time - start_time)*1000
    return array, mil_elapsed_time
