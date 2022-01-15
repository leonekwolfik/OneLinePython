import numpy as np

# [rano, popoludnie, wieczor]

solar_x = np.array(
    [[1,2,3],
     [2,2,5]]
)

# średnia ważona
print(np.average(solar_x, axis=0))