import random
import time
from new_zbox import z_algo
from zbox_naive import naive_z_algo


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}: {elapsed:.2f}s")
        return result
    return wrapper

z_algo = timing(z_algo)
naive_z_algo = timing(naive_z_algo)


for i in range(3):
    s = "".join(random.choice(['a']) for _ in range(1000_000))
    z_algo(s)
    naive_z_algo(s)



