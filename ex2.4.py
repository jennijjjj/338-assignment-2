import json
import time
import matplotlib.pyplot as plt

def func1(array, start, end):
    stack = [(start, end)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = func2(array, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

def func2(array, start, end):
    pi = array[start]
    low = start + 1
    high = end
    while low <= high:
        while low <= high and array[high] >= pi:
            high = high - 1
        while low <= high and array[low] <= pi:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
    array[start], array[high] = array[high], array[start]
    return high

if __name__ == '__main__':
    with open("ex2.json", "r") as f:
        data = json.load(f)

    times = []

    for arr in data:
        start_time = time.time()
        func1(arr, 0, len(arr) - 1)
        end_time = time.time()
        execution_time = end_time - start_time
        times.append(execution_time)

    plt.plot(times)
    plt.xlabel("Array Index")
    plt.ylabel("Execution Time (s)")
    plt.title("Sorting Performance")
    plt.show()


