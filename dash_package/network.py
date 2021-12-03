import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import json
import os

# For plotly network graph
import plotly.graph_objects as go
import networkx as nx

# Import dash app and functions
from dash_package import app
from dash_package.functions import *


# Create app layout
app.layout = html.Div([
    # Button to navigate to home page
    dcc.Link(html.Button('Home'), href='/', refresh=True),
    # Title
    html.H1("Network Recommendation Engine", style={'text-align': 'center'}),
    
    # Create drop down menu
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[
            {'label': 'Naruto Shippuden', 'value': 'naruto'},
            {'label': 'One Piece', 'value': 'onepiece'},
            {'label': 'Black Clover', 'value': 'black_clover'},
            {'label': 'Jumanji: The Next Level', 'value': 'jumanji'},
            {'label': 'Star Trek: The Original Series', 'value': 'startrek'},
            {'label': 'The Office', 'value': 'office'}
            ],
            value='naruto' #set as default because of inspiration
        ),
    html.Div(id='dd-output-container', children=[])
    ]),
    html.Br(),

    # Create slider
    dcc.Slider(
        id='my-slider',
        min=0,
        max=100,
        step=1,
        value=100,
    ),
    html.Div(id='slider-output-container', children=[]),
    html.Br(),
    

    html.Div([
        dcc.Graph(id='network_graph', figure={})
    ])
])

# @app.callback(
#     Output('dd-output-container', 'children'),
#     Input('demo-dropdown', 'value')
# )

# Connect the Plotly graph with Dash Components
@app.callback(
    [Output(component_id='dd-output-container', component_property='children'),
     Output(component_id='slider-output-container', component_property='children'),
     Output(component_id='network_graph', component_property='figure')],
    [Input(component_id='dropdown', component_property='value'),
     Input(component_id='my-slider', component_property='value')]
)

# Function to update graph output
def update_graph(dd_value, slider_value):
    
    #Make appearance better
    name = ""
    if dd_value == "naruto":
        name = "Nartuo Shippuden"
    elif dd_value == "onepice":
        name = "One Piece"
    elif dd_value == "black_clover":
        name = "Black Clover"
    elif dd_value == "jumanji":
        name = "Jumanji: The Next Level"
    elif dd_value == "startrek":
        name = "Star Trek: The Original Series"
    elif dd_value == "office":
        name = "The Office"

    #container = "You have selected: {}".format(name)
    container = "You have selected: " + name
    container2 = "Minimum number of shared actors you want to visualize: {}".format(slider_value) 

    edge_trace, node_trace = create_graph(dd_value, slider_value)

    # Plotly Express graph
    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Node Connections Based on Shared Actors',
                    title_x = 0.5,
                    titlefont=dict(size=22),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Note: Graph omits nodes with degress less than threshold, however, degrees reflect the number of total connections prior to omitting nodes",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002) ], template = 'plotly_dark',
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    return container, container2, fig


# Run App
if __name__ == '__main__':
    app.run_server(debug=True)

