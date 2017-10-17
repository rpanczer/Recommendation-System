import numpy as np
import time

start = time.time()
ratings = np.array([
    5,
    4,
    3,
    2,
    1,
    1,
    5,
    4,
    3,
    5
])

ratings *= 2
end = time.time()
print(ratings)
print(end - start)