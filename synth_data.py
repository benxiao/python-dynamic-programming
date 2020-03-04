import faker
import random
from pandas import DataFrame
import numpy as np
from numpy import vectorize
from datetime import date, timedelta
import time
from typing import *

faker.generator.random.seed(42)
LOCALES = ['en_AU', 'en_CA', 'en_NZ', 'en_US', 'en_GB']
faker_object = faker.Faker(LOCALES)

TOTAL_NUMBER_OF_CHILDREN = 1000
MALE_PERCENTAGE = 0.5
CHILD_AGE_LOW = 5
CHILD_AGE_HIGH = 18
SIBLING_DISTRIBUTION = [0.33, 0.39, 0.22, 0.05, 0.01]

num_siblings = (np.array(SIBLING_DISTRIBUTION) * TOTAL_NUMBER_OF_CHILDREN).astype(np.int)
num_sibling_groups = (num_siblings / np.arange(1, 6)).astype(np.int)

EMAIL_DOMAINS = ['gmail', 'icloud', 'yahoo', 'me', 'hotmail', 'outlook']

# parent age should tie to child age

start = time.time()

n_male_records = int(TOTAL_NUMBER_OF_CHILDREN * MALE_PERCENTAGE)
n_female_records = int(TOTAL_NUMBER_OF_CHILDREN * (1 - MALE_PERCENTAGE))

ids = np.arange(n_female_records + n_male_records)

genders = np.random.choice(['m', 'f'], TOTAL_NUMBER_OF_CHILDREN, p=[MALE_PERCENTAGE, 1 - MALE_PERCENTAGE])

first_names = np.array([faker_object.first_name_male() if g == 'm' else faker_object.first_name_female()
                        for g in genders])

print(f"{first_names.shape=}")


def generate_sibling_ids() -> List[int]:
    result = []
    x = 0
    for i, group_count in enumerate(num_sibling_groups, start=1):
        for _ in range(group_count):
            for _ in range(i):
                result.append(x)
            x += 1

    while len(result) < TOTAL_NUMBER_OF_CHILDREN:
        result.append(x)

    return result


sibling_ids = generate_sibling_ids()


def generate_last_names(sibling_ids: List[int]) -> List[str]:
    result = []
    prev = None
    for i in sibling_ids:
        if prev != i:
            result.append(faker_object.last_name())
            prev = i
        else:
            result.append(result[-1])
    return result


last_names = np.array(generate_last_names(sibling_ids))
print(f"{last_names.shape=}")
#
middle_names = np.array([faker_object.first_name_male() if g == 'm' else faker_object.first_name_female()
                        for g in genders])

print(f"{middle_names.shape=}")

birth_dates = np.array([faker_object.date_of_birth(
                        minimum_age=CHILD_AGE_LOW,
                        maximum_age=CHILD_AGE_HIGH)
                        for _ in range(TOTAL_NUMBER_OF_CHILDREN)])

print(f"{birth_dates.shape=}")


@vectorize
def email_gen(first_name, middle_name, last_name, birth_date) -> str:
    domain = random.choice(EMAIL_DOMAINS)

    # full name

    def t0():
        return f"{first_name}.{last_name}@{domain}.com"

    # initials and birth year
    def t1():
        return f"{first_name[0]}{middle_name[0]}{last_name[0]}{birth_date.year}@{domain}.com"

    def t2():
        return f"{first_name}{birth_date.month}{birth_date.day}@{domain}.com"

    t = random.choice([t0, t1, t2])
    return t()


emails = email_gen(first_names, middle_names, last_names, birth_dates)
print(f"{emails.shape=}")

children = DataFrame({
    "id": ids,
    "sibling_id": sibling_ids,
    "first_name": first_names,
    "middle_name": middle_names,
    "last_name": last_names,
    "birth_date": birth_dates,
    "email_address": emails,
    "gender": genders,
    "is_child": [True] * TOTAL_NUMBER_OF_CHILDREN
})

print(children.head(30).to_markdown(), end='\n'*4)


def mother_birth_date_gen(child_birth_date: date) -> date:
    return child_birth_date - timedelta(days=random.randint(20 * 365, 40 * 365))


def father_birth_date_gen(child_birth_date: date) -> date:
    return child_birth_date - timedelta(days=random.randint(18 * 365, 50 * 365))


def generate_parents(children_df: DataFrame) -> DataFrame:
    parents = children_df.drop_duplicates(subset=['sibling_id'])
    n_pair_parents = len(parents)
    parents = parents.append(parents.copy()).sort_values('id')
    parent_genders = ['m', 'f'] * n_pair_parents

    parents.loc[:, 'gender'] = parent_genders
    parents.loc[:, 'first_name'] = [
        faker_object.first_name_male() if g == 'm' else faker_object.first_name_female()
        for g in parent_genders
    ]
    parents.loc[:, 'middle_name'] = [
        faker_object.first_name_male() if g == 'm' else faker_object.first_name_female()
        for g in parent_genders
    ]
    #
    parents.loc[:, 'last_name'] = [
        last if g == 'm' else faker_object.last_name() if random.random() > 0.5 else last
        for last, g in zip(parents['last_name'], parent_genders)
    ]
    #
    parents.loc[:, 'birth_date'] = [
        father_birth_date_gen(bd) if g == 'm' else mother_birth_date_gen(bd)
        for bd, g in zip(parents['birth_date'], parent_genders)
    ]
    #
    parents.loc[:, 'email_address'] = email_gen(
        parents.loc[:, 'first_name'],
        parents.loc[:, 'middle_name'],
        parents.loc[:, 'last_name'],
        parents.loc[:, 'birth_date']
    )

    parents.loc[:, 'is_child'] = [False] * len(parents)
    parents.loc[:, 'id'] = np.arange(len(parents)) + len(children_df)
    print(parents.head(30).to_markdown())


parents = generate_parents(children)


print(f"elapsed time: {time.time() - start:.2f}s")
