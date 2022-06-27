import multiprocessing
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

    return prime


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    result_async = [pool.apply_async(primeIdentifier, args=(i, )) for i in
                    primeIdentifier(1)]
    results = [r.get() for r in result_async]
    print("Output: {}".format(results))
