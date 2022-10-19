def test_header_names(load_test_data, load_actual_data) -> None:
    """
    Tests whether the headers are named as expected.
    :param load_test_data: the test data we load using pandas
    :param load_actual_data: the actual data we load using the implementation
    """
    # Get test data and actual data
    test_data = load_test_data
    actual_data = load_actual_data

    # Get expected and actual header names
    expected_header_names = set(test_data.columns)
    actual_header_names = set(actual_data[0].keys())

    # Test whether header names are as expected
    msg = f"The column names are incorrect! Expected {expected_header_names} " \
          f"but got {actual_header_names}"
    assert expected_header_names == actual_header_names, msg


def test_data_length(load_test_data, load_actual_data) -> None:
    """
    Tests whether the amount of entries is as expected.
    :param load_test_data: the test data we load using pandas
    :param load_actual_data: the actual data we load using the implementation
    """
    # Get test and actual data
    test_data = load_test_data
    actual_data = load_actual_data

    # Get the amount of entries in each of them
    expected_row_amount = test_data.shape[0]
    actual_row_amount = len(actual_data)

    # Test whether amount of rows is as expected
    msg = f"The amount of rows is incorrect! Expected {expected_row_amount} " \
          f"but got {actual_row_amount}"
    assert expected_row_amount == actual_row_amount, msg


def test_data_content(load_actual_data) -> None:
    """
    Tests whether the loaded data contains fitting data.
    :param load_actual_data: the actual data we load using the implementation
    """
    # Get actual data
    actual_data = load_actual_data

    # Get expected and actual properties
    expected_list_type = list
    expected_nested_list_type = dict

    actual_list_type = type(actual_data)
    actual_nested_list_type = type(actual_data[0])

    # Error messages
    msg_list = f"Your data loader did not output a list! Got {actual_list_type} instead"
    msg_nested_list = f"Your data loader output a list, but that list did not contain dicts! Got {actual_nested_list_type} instead"

    assert expected_list_type == actual_list_type, msg_list
    assert expected_nested_list_type == actual_nested_list_type, msg_nested_list
