"""
JBI010: Assignment 2
Authors: Gijs Walravens

Copyright (c) 2022 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import csv
from typing import List, Dict, Type

# // BEGIN_TODO [task_2] Loading and preparing the dataset

def read_dataset(data_path: str) -> List[Dict[str, any]]:
    """
    Reads in the *subject* data from the file, cleans it up and returns it as a
    list of dicts.
    :param data_path: the path to the CSV file
    :return: list of dicts of the prepared data.
    """
    
    data_list = []
    with open(data_path) as f:
        title = f.readline()
        title = title.rstrip()
        com_title = title.split(',')
        com_title[0] = 'Name_ID'
        for i in f:
            i = i.split(',')
            data_dict = {}
            j = 0 
            for element in com_title:
                if element == 'Name_ID' or element == 'Price':
                    data_dict[element] = int(i[j].rstrip(' >'))
                    j += 1
                else:
                    data_dict[element] = i[j].rstrip()
                    j += 1
            data_list.append(data_dict)
    return data_list

# // END_TODO [task_2]
