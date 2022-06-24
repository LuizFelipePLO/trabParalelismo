from random import randint
import time


def insertion_sort(array):

    for i in range(1, len(array)):

        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array


if __name__ == "__main__":

    array = [randint(0, 100000) for i in range(5)]
    print("Initial array: ")
    print(*array, sep=", ")
    print()

    start_time = time.perf_counter_ns()
    insertion_sort(array)
    end_time = time.perf_counter_ns()

    formattedCounter = (end_time - start_time)

    print("Organized array: ")
    print(*array, sep=", ")

    print()
    print("Process time: ", end_time - start_time, "nanoseconds")
