"""
JBI010: Assignment 2
Authors: Gijs Walravens

Copyright (c) 2022 - Eindhoven University of Technology, The Netherlands
This software is made available under the terms of the MIT License.
"""

import math
import re
import dash
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objs
import plotly.graph_objs as go
import requests
from typing import List, Dict, Tuple
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc


def create_dashboard(data: List[Dict[str, any]]) -> Dash:
    """
    Initializes the dashboard with layout, content and interactivity.
    :param data: the prepped data loaded from the CSVs
    :return: dashboard object that is ready to deploy.
    """
    # Turn the data into a DF
    data = pd.DataFrame(data)

    # Set some options for clearer printing
    pd.options.display.max_columns = None
    pd.options.display.max_rows = None

    # Create Dash app object with correct path and styling
    app = dash.Dash(__name__
                    , assets_folder="../assets"
                    , external_stylesheets=
                    [dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])

    # Retrieve all item names for the dropdown
    all_names = np.sort(data["Name"].unique())

    # region Layout
    app.layout = html.Div([
        # Navigation bar on top of the page
        dbc.Navbar(
            dbc.Container([
                dbc.Row([
                    # Navbar logo
                    dbc.Col(
                        html.Img(src=app.get_asset_url("GE_logo.png"), height="30px")
                    ),
                    # Navbar text
                    dbc.Col(
                        dbc.NavbarBrand("Grand Exchange Dashboard", className="ms-2", style={"color": "white"})
                    )
                ], align="center", className="g-0")
            ]), color="dark", style={"margin": "0px 0px 12px 0px"}
        ),
        # Main body
        dbc.Container([
            # Item selection card
            dbc.Card([
                dbc.Row([
                    # Thumbnail image
                    dbc.Col(
                        html.Img(src="../assets/placeholder.gif", id="thumbnail"), width=1),
                    # Dropdown
                    dbc.Col(
                        dcc.Dropdown(
                            id="item-select",
                            options=[{"label": i, "value": i} for i in all_names],
                            value=all_names[0]
                        ), width=11
                    )
                ], align="center"),
                dbc.Row(
                    # Item link button
                    dbc.Col(
                        dbc.Button("Grand Exchange item link", className="me-1", target="_blank",
                                   href="https://secure.runescape.com/m=itemdb_rs/", id="item-link")
                    ), style={'margin': '15px 0px 0px 0px'}
                )
            ], body=True, style={'margin': '0px 0px 12px 0px'}),
            # Holder for analysis graphs
            html.Div([
                dbc.Row([
                    dbc.Col(
                        # Line graph card
                        dbc.Card(
                            dcc.Graph(
                                id="line-graph"
                            ), body=True
                        ), width=7
                    ),
                    dbc.Col([
                        # Percent difference card
                        dbc.Card([
                            html.H4("Percent difference in item value between first and last recorded datapoints",
                                    style={'textAlign': 'center'}),
                            dbc.Row([
                                dbc.Col([
                                    html.Div([
                                        html.I(id="change_percent_arrow", className="bi bi-arrow-up",
                                               style={'color': 'lime', 'fontSize': '3em'}),
                                        html.Span("100%", id="change_percent", className="display-3",
                                                  style={'color': 'lime', 'textAlign': 'center'})
                                    ], className="d-flex justify-content-center")
                                ], width=12)
                            ]),
                            dbc.Row([
                                dbc.Col([
                                    html.P("Year 1", id="old_date", className="display-6",
                                           style={'textAlign': 'center'}),
                                    html.P("BEFORE", id="old_price", className="display-6",
                                           style={'textAlign': 'center'})
                                ], width=6
                                ),
                                dbc.Col([
                                    html.P("Year 2", id="new_date", className="display-6",
                                           style={'textAlign': 'center'}),
                                    html.P("AFTER", id="new_price", className="display-6",
                                           style={'textAlign': 'center'})
                                ], width=6
                                )
                            ])
                        ], body=True, style={'margin': '0px 0px 12px 0px'}),

                        # // BEGIN_TODO [task_5.a] Create the card
                        # card with text
                        dbc.Card(
                            dbc.CardBody(
                                [
                                    html.P(
                                        "empty",
                                         id = "text0",
                                         className = "card-text"
                                        )
                                    ],
                                    ))
                        # // END_TODO [task_5.a]
                    ])]
                )
            ])
        ]),
        # Data storage
        dcc.Store(id="item-data")
    ])

    # endregion

    # region Functionalities
    # region Storing and loading selected item's data in browser session
    @app.callback(
        Output("item-data", "data"),
        Input("item-select", "value")
    )
    def store_item_value(input_val: str) -> str:
        """
        Callback to retrieve the data of the selected item and store it for
        later usage.
        :param input_val: the data from the item selection dropdown
        :return: the data of the currently selected item serialized to JSON.
        """
        # Retrieve the data for the selected item
        item_data = data.loc[data["Name"] == input_val]
        # Store it in the browser for later use
        return item_data.to_json(orient="split")

    def read_item_value(stored_data: str) -> pd.DataFrame:
        """
        Loads the serialized JSON data of the selected item from the user's
        browser and turns it back into a DataFrame.
        :param stored_data: the JSON data of the item
        :return: the data of the selected item in the form of a DataFrame.
        """
        # First check if the data is actually stored
        if stored_data is None:
            # If not, then prevent Dash from doing an update
            return dash.no_update

        # Retrieve data that belongs to the selected item
        item_data = pd.read_json(stored_data, orient="split")

        # Parse the date table back to the right formatting
        item_data["Date"] = item_data["Date"].dt.strftime("%Y-%m-%d %H:%M:%S")

        return item_data

    # endregion
    # region Update the line graph
    @app.callback(
        Output("line-graph", "figure"),
        Input("item-data", "data")
    )
    def update_line_graph(stored_data: str) -> plotly.graph_objs.Figure:
        """
        Callback to update the line graph to the data of the currently selected
        item.
        :param stored_data: data of the currently selected item in the dropdown
        :return: a new Plotly line graph for the currently selected item.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        # Define the figure
        fig = go.Figure()

        # // BEGIN_TODO [task_4.a] Adding a line graph

        fig = px.line(item_data, x = 'Date', y = 'Price')
        

        # // END_TODO [task_4.a]

        return fig

    # endregion
    # region Update the price difference card
    @app.callback(
        Output('change_percent_arrow', 'className'),
        Output('change_percent_arrow', 'style'),
        Output('change_percent', 'children'),
        Output('change_percent', 'style'),
        Output("old_date", "children"),
        Output("old_price", "children"),
        Output("new_date", "children"),
        Output("new_price", "children"),
        Input("item-data", "data")
    )
    def update_price_diff(stored_data: str) -> Tuple[any, ...]:
        """
        Callback to update the card containing the percentage difference in
        price between the first and last recorded datapoints of the selected
        item, together with those dates and prices for those dates.
        :param stored_data: data of the currently selected item in the dropdown
        :return: a tuple containing all the new values and style settings
        depending on those values.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        # Get the first and last recorded date
        first_date = extract_date(item_data["Date"].min())
        last_date = extract_date(item_data["Date"].max())

        # Get the first and last price
        first_price = (item_data.loc[item_data["Date"].str.contains(first_date)].iloc[0])["Price"]
        last_price = (item_data.loc[item_data["Date"].str.contains(last_date)].iloc[0])["Price"]

        # Calculate the relative change in percentages
        relative_change = calculate_relative_change(first_price, last_price)

        # Check whether the relative change is positive or negative
        # , set color and icon accordingly to that
        if "-" in relative_change:
            icon_class = "bi bi-arrow-down"
            icon_style = {'color': 'red', 'fontSize': '3em'}
            percentage_style = {'color': 'red', 'textAlign': 'center'}
        else:
            icon_class = "bi bi-arrow-up"
            icon_style = {'color': 'lime', 'fontSize': '3em'}
            percentage_style = {'color': 'lime', 'textAlign': 'center'}

        return icon_class, icon_style, relative_change, percentage_style, \
               first_date, f'{first_price:,d}', last_date, f'{last_price:,d}'

    def extract_date(timestamp: str) -> str:
        """
        Takes a timestamp and extracts only the data part.
        :param timestamp: a string in the format of "YYYY-MM-DD 00:00:00.00"
        :return: only the data part of the timestamp.
        """

        # // BEGIN_TODO [task_4.b] Extracting date from a string

        mode = re.compile(r'\w+\-\w+\-\w+')
        a = mode.search(timestamp)
        return a.group()

        # // END_TODO [task_4.b]

    def calculate_relative_change(price_1: int, price_2: int) -> str:
        """
        Calculates the difference in price between the first recorded datapoint
        and the last, returning a percentage value.
        :param price_1: the first recorded price
        :param price_2: the last recorded price
        :return: a percentage value of the difference in price.
        """

        # // BEGIN_TODO [task_4.c] Calculating the relative change percentage

        num = (price_2 - price_1)/price_1
        str_num = str(round(num * 100,2)) + '%'
        
        return str_num
        
        # // END_TODO [task_4.c]

    # endregion
    # region Update the item link button
    @app.callback(
        Output("item-link", "href"),
        Input("item-data", "data")
    )
    def update_item_link(stored_data: str) -> str:
        """
        Callback to update the Grand Exchange item link to the URL of the
        currently selected item.
        :param stored_data: date of the currently selected item in the dropdown
        :return: URL of the GE page for the currently selected item.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        # Return the URL for that item
        return item_data["Name_URL"].iloc[0]

    # endregion
    # region Update the item thumbnail image
    @app.callback(
        Output("thumbnail", "src"),
        Input("item-data", "data")
    )
    def update_thumbnail(stored_data: str) -> str:
        """
        Callback to update the thumbnail to a picture of the currently selected
        item.
        :param stored_data: data of the currently selected item in the dropdown
        :return: an image URL pulled from the GE website.
        """
        # Retrieve the stored item data
        item_data = read_item_value(stored_data)

        # Define image formats
        image_formats = ("image/png", "image/jpg", "image/gif")

        # Retrieve the ID and URL that belongs to the selected item
        item_id = item_data["Name_ID"].iloc[0]
        item_url = item_data["Name_URL"].iloc[0]

        # Request the image URL
        url_request = requests.get(item_url)
        img_url = re.search("https://secure[.]runescape[.]com/m=itemdb_rs/[0-9]+_obj_big.gif[?]id=" + str(item_id),
                            url_request.text)
        img_url = img_url.group(0)

        # Get the image header to check for a correct image link
        r = requests.head(img_url)
        if r.headers["content-type"] in image_formats:
            return img_url

        # If no valid image is found, prevent dash from doing an update
        return dash.no_update

    # endregion
    # region Update the GP to VED card
    # // BEGIN_TODO [task_5.b] Creating the functions for your own card

    @app.callback(
        Output('text0','children'),
        Input('item-data','data')
    )
    def update_gp_to_ved_card(stored_data: str) -> str:
        """
        callback function return string
        """
        item_data = read_item_value(stored_data)
        date = extract_date(item_data["Date"].max())
        price = (item_data.loc[item_data["Date"].str.contains(date)].iloc[0])["Price"]
        number_of_bolivars = convert_gp_to_ved(price)
        hours = calculus_hours_needed(number_of_bolivars)
        item = item_data["Name"].max()
        return f"On {date} {item} was worth {price}, about the equivalent \
                 of {number_of_bolivars} Venezuelan Bolivars. Someone working a minimum wage \
                 job in Venezuela would need to work {hours} hours in order to afford this item."



    def convert_gp_to_ved(price: str) -> str:
        """
        auxiliary function, which is used to convert gp to VED
        """
        price = int(price) / 1000000
        return str(price / 0.06 * 7.97)

    def calculus_hours_needed(price: str) -> str:
        """
        auxiliary function, which is used to compute how hours do people need to certain item
        """
        hours = float(price) / (130 / (40 * 4))
        return str(hours)
    # // END_TODO [task_5.b]
    # endregion
    # endregion

    return app



