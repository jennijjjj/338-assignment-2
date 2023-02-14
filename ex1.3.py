
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

