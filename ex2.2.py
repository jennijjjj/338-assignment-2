import sys
import json
import time
import matplotlib.pyplot as plt
import multiprocessing
import time

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pi = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pi:
            high = high - 1
        while low <= high and array[low] <= pi:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def sort_array(array):
    func1(array, 0, len(array) - 1)
    return array

def split_array(array, chunk_size):
    chunks = [array[i:i + chunk_size] for i in range(0, len(array), chunk_size)]
    return chunks

def divide_and_conquer(array, chunk_size=1000):
    chunks = split_array(array, chunk_size)
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    sorted_chunks = pool.map(sort_array, chunks)
    pool.close()
    pool.join()
    return sorted(sorted_chunks)

if __name__ == '__main__':
    with open("ex2.json", "r") as f:
        data = json.load(f)

    times = []

    for arr in data:
        
        if len(arr) <=3000:
            start_time = time.time()
            func1(arr, 0, len(arr) - 1)
            end_time = time.time()
        else:
            start_time = time.time()
            divide_and_conquer(arr, chunk_size=1000)
            end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)

    plt.plot(times)
    plt.xlabel("Array Index")
    plt.ylabel("Execution Time (s)")
    plt.title("Sorting Performance")
    plt.show()