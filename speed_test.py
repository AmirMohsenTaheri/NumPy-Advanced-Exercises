import numpy as np
import time

def pure_python():
    t1 = time.time()
    X = range(1000000)
    Y = range(1000000)
    Z = []
    for i in range(1000000):
        Z.append(X[i] + Y[i])
    t2 = time.time()
    return t2 - t1

def numpy_python():
    t1 = time.time()
    X = np.arange(1000000)
    Y = np.arange(1000000)
    Z = X + Y
    t2 = time.time()
    return t2 - t1

def main():
    print(f"python list time: {pure_python()}")
    print(f"numpy time: {numpy_python()}")

main()