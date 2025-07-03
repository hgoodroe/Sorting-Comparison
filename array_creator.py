"""Function for creating arrays"""
import random  # used to
import time


def create_array():
    """function to create an array"""
    random_array = []

    def array_size_selection():
        print('Please enter the number of elements you want to sort: ')
        array_size = input()
        while not array_size.isdigit():
            try:
                array_size = int(array_size)
                if array_size < 0:
                    raise ValueError
            except ValueError:
                print('Please enter a valid integer above 0.')
            array_size = input()
        return array_size

    def min_max(array_size):
        array_min = int(input(
            'What is the smallest number you want in the array? \n'))
        array_max = int(input(
            'What is the largest number you want in the array? \n'))
        start_time = time.time()
        for x in range(int(array_size)):
            random_array.append(random.randint(array_min, array_max))
            x += 1
        end_time = time.time()
        elapsed_time_creation = (end_time - start_time)*1000
        return random_array, elapsed_time_creation, array_min, array_max, array_size,

    array_size = array_size_selection()
    random_array, elapsed_time_creation, array_min, array_max, array_size = min_max(
        array_size)

    return random_array, elapsed_time_creation, array_min, array_max, array_size
