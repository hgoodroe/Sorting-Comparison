"""User interface & directive function for sorting user-created arrays"""

import json
import threading
import time
from array_creator import create_array
from bubble_sort import sorter_1
from quick_sort import sorter_2
from monkey_sort import sorter_3
from records_logger import records_log

PROCESSING = False


def main():
    """Main Function for dictating program"""
    global PROCESSING
    is_sorted = False
    is_reversed = False
    spinner_thread = None
    elapsed_time_sort = "No Time Recorded"

    def start_loading():
        global PROCESSING
        PROCESSING = True
        spinner_thread = threading.Thread(target=loading)
        spinner_thread.start()
        return spinner_thread

    def loading():
        symbols = ["-", "\\", "|", "/"]
        while PROCESSING:
            for symbol in symbols:
                print(f"Loading... {symbol}", end="\r")
                time.sleep(0.1)  # Adjust this for spinner speed
        print("Sorting complete!        ")

    def end_loading(spinner_thread):
        global PROCESSING
        PROCESSING = False
        spinner_thread.join()

    def array_type_selection():
        print("Enter letter of the the type of array you want to sort.  ")
        print("\n A) sorted \n B) reverse array \n C) random array \n")
        array_type = input("Please provide a  choice: ")

        while array_type not in ("A", "B", "C"):
            print("Please enter a valid choice.")
            array_type = input("Please provide a  choice: ")
        return array_type

    def array_sort_selection():
        print("Enter the letter of the sorting method you want to use.")
        print("Input: ")
        print("\n A) bubble sort \n B) quick sort \n C) monkey sort \n")
        array_sort = input(("Please provide a  choice: "))
        while array_sort not in ("A", "B", "C"):
            print("Please enter a valid choice.")
            array_sort = input("Please provide a  choice: ")
        return array_sort

    def sort_results(data_set_selection, sorted_array):
        if len(data_set_selection) > 100:
            output_data = {
                "Unsorted Array": data_set_selection,
                "Sorted Array": sorted_array}

            end_data = {}
            for key in output_data:
                end_data[key] = []
                for i in range(0, len(output_data[key]), 20):
                    data = output_data[key][i:i+20]
                    end_data[key].extend(data)

            with open("Arrays.json", 'w', encoding='utf-8') as json_file:
                json.dump(output_data, json_file, indent=4)

        else:
            print('\nUnsorted Array: ')
            for i in range(0, len(data_set_selection), 20):
                print(data_set_selection[i:i+20])
            print('\nSorted Array: ')
            for i in range(0, len(sorted_array), 20):
                print(sorted_array[i:i+20])

    rand_array, elapsed_time_creation, array_min, array_max, array_size = create_array()

    array_type = array_type_selection()

    array_sort = array_sort_selection()

    original_array = rand_array
    match array_type:
        case "A":
            sorted_data_set = sorted(rand_array)
            is_sorted = True
        case "B":
            reverse_data_set = sorted(
                rand_array, reverse=True)
            is_reversed = True
        case "C":
            data_set = rand_array
            is_sorted = False
            print("\nArray Creation Elapsed Time: ",
                  elapsed_time_creation, " ms")

    if is_sorted is True:
        original_array = sorted_data_set
    elif is_reversed is True:
        original_array = reverse_data_set
    elif is_sorted is False:
        original_array = data_set

    match array_sort:
        case "A":
            try:
                spinner_thread = start_loading()
                print("Starting sorting...")
                sorted_array, elapsed_time_sort = sorter_1(
                    original_array.copy())
                sort_results(original_array, sorted_array)
            finally:
                end_loading(spinner_thread)
                print("\nBubble Sort Total Elapsed Time : ",
                      elapsed_time_sort, " ms")
        case "B":
            try:
                spinner_thread = start_loading()
                print("Starting sorting...")
                sorted_array, elapsed_time_sort = sorter_2(
                    original_array.copy())
                sort_results(original_array, sorted_array)
            finally:
                end_loading(spinner_thread)
                print("\nQuick Sort Total Elapsed Time : ",
                      elapsed_time_sort, " ms")
        case "C":
            try:
                spinner_thread = start_loading()
                print("Starting sorting...")
                sorted_array, elapsed_time_sort = sorter_3(
                    original_array.copy())
                sort_results(original_array, sorted_array)
            finally:
                end_loading(spinner_thread)
                print("\nMonkey Sort Total Elapsed Time : ",
                      elapsed_time_sort, " ms")

    records_log(array_type, array_size, array_min,
                array_max, elapsed_time_sort, array_sort, )

    redo = input("Would you like to create a & sort a different array? Y/N\n")
    if redo == "Y":
        main()
    else:
        return ()


if __name__ == '__main__':
    with open("Records.json", 'w', encoding='utf-8') as json_file:
        json.dump([], json_file)  # Write an empty list
    main()
