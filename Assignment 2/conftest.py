import pytest
import pandas as pd
import pytest
from typing import List, Dict
from app import data_loader

data_path = "../data/GE_data.csv"


@pytest.fixture
def load_test_data() -> pd.DataFrame:
    """
    Loads in the data and clean it using Pandas.
    :return: the dataset loaded and cleaned up as we expect it to be.
    """
    # First load in the CSV
    test_data = pd.read_csv(data_path)

    # Make the headers consistent
    test_data.rename(columns={"NAME_ID": "Name_ID"}, inplace=True)

    # Remove unwanted characters
    test_data["Price"] = test_data["Price"].str.replace(">", "")
    test_data["Price"] = test_data["Price"].str.replace(" ", "")

    # Parse necessary strings to ints
    test_data["Price"] = test_data["Price"].astype(int)
    test_data["Name_ID"] = test_data["Name_ID"].astype(int)

    return test_data


@pytest.fixture
def load_actual_data() -> List[Dict[str, any]]:
    """
    Loads in the data using the implemented data loader.
    :return: the (hopefully) loaded in and cleaned dataset.
    """
    # Load the data
    actual_data = data_loader.read_dataset("../data/GE_data.csv")

    return actual_data
