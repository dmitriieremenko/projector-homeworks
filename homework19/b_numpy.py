import numpy as np

a = np.arange(1, 101, 1)
F_a = 2 * a**2 + 5

for i in range(len(a)):
    print(f"F({a[i]}) = {F_a[i]}")
