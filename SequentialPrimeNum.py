from random import randint
import time


def primeIdentifier(array):
    prime = []
    for i in array:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            prime.append(i)

    print("Prime number array: ")
    print(*prime, sep=", ")
    return prime


if __name__ == "__main__":

    array = [randint(0, 100000) for i in range(5)]
    print("Initial array: ")
    print(*array, sep=", ")
    print()

    start_time = time.perf_counter_ns()
    primeIdentifier(array)
    end_time = time.perf_counter_ns()

    formattedCounter = (end_time - start_time)

    print()
    print("Process time: ", end_time - start_time, "nanoseconds")
