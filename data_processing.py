import csv
import io
import random
import pandas as pd
from collections import defaultdict


def process_values(input1, input2, input3):
    input1 = int(input1)
    input2 = int(input2)
    input3 = int(input3)

    df = pd.DataFrame()
    my_dict = defaultdict(list)

    for i in range(10):
        my_dict['input1'].append(random.randrange(input1, input2, input3))
        my_dict['input2'].append(random.randrange(input1, input2, input3))
        my_dict['input3'].append(random.randrange(input1, input2, input3))
        my_dict['input4'].append(random.randrange(input1, input2, input3))

    df = pd.DataFrame(my_dict)
    return df


def validate_values(input1, input2, input3):
    if not all(i.isdigit() for i in [input1, input2, input3]):
        return True
