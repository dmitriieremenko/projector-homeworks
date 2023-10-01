import numpy as np

a = np.arange(-10, 11, 1)
F_a = np.exp(-a)

for i in range(len(a)):
    print(f"F({a[i]}) = {F_a[i]}")
