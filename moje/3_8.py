import random

import numpy as np


#
def show_array_info(arr: np.ndarray):
    print(arr)
    print(f"ndim={arr.ndim}")
    print(f"shape={arr.shape}")
    print("\n\n")


a = np.array([1, 2, 3, 4])
show_array_info(a)

b = np.array([[random.randint(0, 5) for _ in range(3)] for _ in range(3)])
show_array_info(b)

c = np.array([[[random.randint(0, 5) for _ in range(3)] for _ in range(3)] for _ in range(2)])
show_array_info(c)
