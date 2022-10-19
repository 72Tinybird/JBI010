from cgi import test
import pandas as pd
import pytest
from typing import List, Dict
from app import data_loader
from app import eda

# // BEGIN_TODO [task_3.e] PyTests for mean and median
def test_compute_mean() ->None:
    assert eda.compute_mean([{'Name': 'Item A', 'Price': 1000}, {'Name':'Item B', 'Price': 1200}]) == 1100

def test_compute_median() ->None:
    assert eda.compute_median([{'Name': 'Item A', 'Price': 3}, {'Name':'Item B', 'Price': 6}, {'Name': 'Item B', 'Price': 12}]) == 6
#
# // END_TODO [task_3.e]
