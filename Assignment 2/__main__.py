"""
JBI010: Assignment 2
Authors: Gijs Walravens

Copyright (c) 2022 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import data_loader
import eda
import dashboard

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Load in the data and prep it
    data = data_loader.read_dataset("../data/GE_data.csv")

    # Run Dashboard? (set to True to run Dash, set to False for console printing)
    # Leave this on false until you are done with the data prep and EDA exercises!
    dash_mode: bool = True

    if dash_mode:
        my_dashboard = dashboard.create_dashboard(data)
        my_dashboard.run_server(debug=False)
    else:
        eda.explore(data)
