from numba import typeof
import numpy as np
NB_BYTES = typeof("".encode())
NB_1D_INT64_ARRAY = typeof(np.ones(1, dtype=np.int64))
