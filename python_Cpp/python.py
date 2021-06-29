import numpy as np
import test

a = np.array([1,2]).astype(np.float32)
b = np.array([2,3]).astype(np.float32)

c = test.add_arrays(a,b)
d = test.sum(1,2)
print(c,d)
