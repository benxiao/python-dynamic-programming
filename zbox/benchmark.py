import random
import time
from zbox import z_algo as jit_z
from jit_zbox import z_algo as python_z


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}: {elapsed:.4f}s")
        return result
    return wrapper


jit_z = timing(jit_z)
python_z = timing(python_z)


for i in range(3):
    s = "".join(random.choice(['a', 'b', 'c']) for _ in range(1000_000))
    jit_z(s)
    python_z(s)



