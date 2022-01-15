import numpy as np

sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(['Jan', 'Robert', 'Alicja', 'Jozef', 'Joanna', 'Franciszek', 'Karol'])

print(students[np.argsort(sat_scores)[:-4:-1]])