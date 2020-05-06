from jit_robin_karp import jit_robin_karp
from robin_karp import robin_karp2, robin_karp
import random
import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"{func.__name__}: {elapsed:.5f}s")
        return result
    return wrapper


robin_karp = timing(robin_karp)
robin_karp2 = timing(robin_karp2)
jit_robin_karp = timing(jit_robin_karp)
python_find = timing(str.find)
pattern = "aaaaaaa"
for _ in range(10):
    s = "".join(random.choice(['a', 'b', 'c']) for _ in range(1000))
    print(robin_karp2(s, pattern))
    robin_karp(s, pattern)
    print(jit_robin_karp(s.encode(), pattern.encode()))
    # python_find(s, pattern)

