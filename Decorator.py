def benchmark(iters: int):

    def out_iterator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                print('iters = ', i)
                total = total + end - start

            print('[*] Running Time: {} ms.'.format(total / iters * 1000))


        return wrapper

    return out_iterator

def cache(func):
    values = {}

    def wrapped(x):
        if x not in values.keys():
            values[x] = func(x)
        return values[x]
    return wrapped


@benchmark(iters=10)
def factorial(n: int) -> int:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact


factorial(10000)



