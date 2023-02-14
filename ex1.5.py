import timeit
import matplotlib.pyplot as plt
import numpy as np

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

n_values = list(range(36))
time_values = []

for n in n_values:
    time_elapsed = timeit.timeit(lambda: func(n), number=1)
    time_values.append(time_elapsed)

plt.plot(n_values, time_values)
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("n vs Time to Compute n")
plt.show()




memoize = {}

def func(n):
    if n in memoize:
        return memoize[n]

    else:
        if n <= 2:
            fib = 1
        else:
            fib = func(n-1) + func(n-2)
            memoize[n] = fib

    return fib

n_values = list(range(50))
time_values = []

for n in n_values:
    time_elapsed = timeit.timeit(lambda: func(n), number=1)
    time_values.append(time_elapsed)

plt.plot(n_values, time_values, label="Actual")
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("n vs Time to Compute n")

z = np.polyfit(n_values, time_values, 1)
p = np.poly1d(z)
plt.plot(n_values, p(n_values), label="Approximation trendline")

plt.legend()
plt.show()

