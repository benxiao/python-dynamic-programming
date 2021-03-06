import pandas as pd
from pandas import DataFrame
import faker
import random
import metaphone
import itertools
from jellyfish import damerau_levenshtein_distance
from numpy import vectorize
import time
import tqdm
from multiprocessing.pool import Pool

damerau_levenshtein_distance = vectorize(damerau_levenshtein_distance)
doublemetaphone = vectorize(metaphone.doublemetaphone)

l = 3000_00
faker = faker.Faker()
gender = [random.choice(['m', 'f']) for _ in range(l)]
first_name = [faker.first_name_male() if g == 'm' else faker.first_name_female() for g in gender]
last_name = [faker.last_name() for _ in range(l)]
birth_date = [faker.date_of_birth(minimum_age=12, maximum_age=15) for _ in range(l)]

data = dict(
    first_name=first_name,
    last_name=last_name,
    gender=gender,
    birth_date=birth_date
)

start = time.time()
df = DataFrame(data)

meta0 = doublemetaphone(df['first_name'])
meta1 = doublemetaphone(df['last_name'])

meta0 = meta0[0]
meta1 = meta1[0]

block = df['gender'] + meta0 + meta1
groups = df.groupby(by=block)


def score(df):
    group_combinations = list(itertools.combinations(df.index.tolist(), 2))
    xs = [r[0] for r in group_combinations]
    ys = [r[1] for r in group_combinations]
    xdf = df.loc[xs]
    ydf = df.loc[ys]
    first_name_cmp = damerau_levenshtein_distance(xdf.first_name, ydf.first_name)
    last_name_cmp = damerau_levenshtein_distance(xdf.last_name, ydf.first_name)
    score = first_name_cmp + last_name_cmp
    result = DataFrame(dict(left=xs, right=ys, score=score))
    return result[result.score < 4]


pool = Pool(16)
print(f"average block size: {sum(len(df) for _, df in groups) / len(groups)}", flush=True)
df_lst = pool.map(score, [df for _, df in tqdm.tqdm(groups) if len(df) > 1])

a = pd.concat(df_lst, axis=0)
print(f"length of matched scored pairs: {len(a)}")
print(time.time() - start)
