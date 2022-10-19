"""
JBI010: Assignment 2
Authors: Gijs Walravens

Copyright (c) 2022 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

from cmath import exp
import plotly.express as px
from typing import List, Dict
# import data_loader as da


def explore(data: List[Dict[str, any]]) -> None:
    """
    Performs EDA on the passed data.
    :param data: the data that will be used in the EDA
    """
    # Parameters used during EDA
    start_date = "2008-06-01"  # The first date from which to lookup items
    end_date = "2022-06-01"  # The second date from which to lookup items
    amount_of_items = 20  # The amount of items to lookup

    # Return the top items from the defined start date and end date
    top_items_2008 = find_top_items_on_date(data, start_date, amount_of_items)
    top_items_2022 = find_top_items_on_date(data, end_date, amount_of_items)

    # Print those top items
    print(f"Top {amount_of_items} most expensive items on {start_date}:")
    print_items(top_items_2008)
    print(f"Top {amount_of_items} most expensive items on {end_date}:")
    print_items(top_items_2022)

    # TODO [task_3.b]
    """
    (Bonus) You may have noticed that some of the top prices have something 
    in common. Give a (computer science) related reason as to why some of these 
    top valued items look so similar.
    ANSWER: 
    Some top prices of 2022 most expensive items are same but they still have a order in the list, because the 
    function sorted is stable enough to avoid the error happening when there are same values, it can sort them 
    in the order in which they appear.
    """

    # Compute the mean of those item prices
    mean_2008 = compute_mean(top_items_2008)
    mean_2022 = compute_mean(top_items_2022)
    print(f"The mean price of top items in 2008 is {mean_2008}")
    print(f"The mean price of top items in 2022 is {mean_2022}")

    # Compute the median of those item prices
    median_2008 = compute_median(top_items_2008)
    median_2022 = compute_median(top_items_2022)
    print(f"The median price of top items in 2008 is {median_2008}")
    print(f"The median price of top items in 2022 is {median_2022}")

    # Drawing the box plots
    draw_box_plot(data, top_items_2008)
    draw_box_plot(data, top_items_2022)

    # TODO [task_3.g]
    """
    (Bonus) Based off the differences in mean, median and box plots between the data 
    from 2008 and 2022, what potential real life economic phenomenon do you see 
    happening in the economy of RuneScape? (hint: it is a hot topic in a lot of 
    real life news currently as well)
    ANSWER: 
    currentcy devaluation is happened in both real life and RuneScape.Suppose the value of items in 2008 and 2022 are same,
    which means the times you spent on getting them are same, but price gains a enormous gap between 2008 and 2022.Take the 
    blue partyhat as a exmpale, the price in 2008 is 380000000, and the price comes to 2147483647 in 2022,which is nearly 7 
    times larger than it in 2008. This situation fits the mean and median number as well, which indicate a inflation in past 
    12 years

    """


def find_top_items_on_date(data: List[Dict[str, any]], date: str, amount : int ) -> List[Dict[str, any]]:
    """
    Retrieves the top valued items for a given date.
    :param data: list of dicts containing all item data
    :param date: the date to retrieve the top items for
    :param amount: the amount of items to retrieve
    :return: a list of dicts where each dict contains an item name, price pair.
    """

    # // BEGIN_TODO [task_3.a] Finding the top items in a year
    """
    top_items = []
    top_item = {'Name':0, 'Price':0}
    for data_line in data:
        if data_line['Date'][0:10] == date:
            if data_line['Price'] >= top_item["Price"]:
                top_item["Price"] = data_line['Price']
                top_item['Name'] = data_line['Name']
    top_items.append(top_item)  
    for j in range(1,21):
        top_item = {'Name':0, 'Price':0}
        for data_line in data:
            if data_line['Date'][0:10] == date:
                if data_line['Price'] >= top_item["Price"] and data_line['Price'] < top_items[j - 1]['Price']:
                    top_item["Price"] = data_line['Price']
                    top_item['Name'] = data_line['Name']
        top_items.append(top_item)
    return top_items [1:21]
    """
    top_items = []
    b = []
    a = sorted(data, key=lambda d: d["Price"], reverse=True)
    for j in a:
        if j['Date'][0:10] == date:    
            b.append(j)     
    for i in range(amount):
        top_items.append({'Name':b[i]['Name'], 'Price':b[i]['Price']})       
    return top_items
    # // END_TODO [task_3.a]


def print_items(items: List[Dict[str, any]]) -> None:
    """
    Function to help neatly print a list of items.
    :param items: the item names and their prices
    """
    if items is None:
        print("Passed list is undefined, not printing anything.")
        return
    for i in range(0, len(items)):
        print(f"[{i + 1}] {items[i]['Name']}: {items[i]['Price']}")
    print("")


def compute_mean(items: List[Dict[str, any]]) -> float:
    """
    Computes the mean price of the given items.
    :param items: list of items with their prices to compute the mean for
    :return: the mean price of the given items.
    """

    # // BEGIN_TODO [task_3.c] Computing the mean
    value_list = []
    for item in items:
        value_list.append(item['Price'])
    mean = sum(value_list)/len(value_list)
    return mean
    # // END_TODO [task_3.c]


def compute_median(items: List[Dict[str, any]]) -> float:
    """
    Computes the median price of the given items.
    :param items: list of items with their prices to compute the mean for
    :return: the median price of the given items.
    """

    # // BEGIN_TODO [task_3.d] Computing the median

    value_list = []
    for item in items:
        value_list.append(item['Price'])
    value_list.sort()
    if len(value_list)%2 == 0:
        median = (value_list[int(len(value_list)/2) - 1] + value_list[int(len(value_list)/2)])/2
    else:
        median = value_list[int(len(value_list)/2)]
    return median
        

    # // END_TODO [task_3.d]


def draw_box_plot(items: List[Dict[str, any]], item_subset: List[Dict[str, any]]) -> None:
    """
    Draws box plots for the given item subset.
    :param items: the list of dicts containing all the item data
    :param item_subset: a selection of items (containing at least their names)
    """

    # // BEGIN_TODO [task_3.f] Drawing a box plot
    items_name = []
    items_price = []
    name_price = []
    for y in item_subset:
        items_name = items_name + [y[x] for x in y if x == 'Name']
    items_price = items_price + [{x['Name']: x['Price']} for x in items if x['Name'] in items_name]
    for name in items_name:
        for price in items_price:
            if name in price:
                name_price.append({'Name':name, 'Price': price[name]})
    z = px.box(name_price, x = 'Name', y = 'Price')
    z.show()

    # // END_TODO [task_3.f]

