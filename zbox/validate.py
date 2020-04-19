from new_zbox import z_algo
from zbox_naive import naive_z_algo
import random
from tqdm import tqdm

import sys
sys.path.append('.')

n_tests = 1000
for i in tqdm(range(n_tests)):
    s = "".join(random.choice(['a', 'b', 'c']) for x in range(1000_000))
    z_values_a = naive_z_algo(s)
    #print(z_values_a)
    z_values_b = z_algo(s)
    #print(z_values_b)
    assert (z_values_a == z_values_b), f"zbox fails at {s}"

print("zbox passes")