import random
import numpy
import time

count = 1000000

start = time.time()
ls = []
for i in range(count):
    ls.append(random.random())
print('Random: ', time.time() - start)

start = time.time()
ls = [random.random() for i in range(count)]
print('Generator: ', time.time() - start)

start = time.time()
ls = numpy.random.random(count)
print('Numpy: ', time.time() - start)