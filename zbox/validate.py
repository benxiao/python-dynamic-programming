from zbox import z_algo as z0
from jit_zbox import z_algo as z1
import random
from tqdm import tqdm

import sys
sys.path.append('.')

n_tests = 1000
for i in tqdm(range(n_tests)):
    s = "".join(random.choice(['a', 'b', 'c']) for x in range(1000_000))
    z_values_a = z0(s)
    #print(z_values_a)
    z_values_b = z1(s)
    #print(z_values_b)
    assert (z_values_a == z_values_b), f"zbox fails at {s}"

print("zbox passes")