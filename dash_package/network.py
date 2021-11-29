import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
import json
import os

# For plotly network graph
import plotly.graph_objects as go
import networkx as nx

from dash_package import app

# Import data
url = 'dash_package/web_scraper/no_games.csv'
df = pd.read_csv(url)


# Create nodelist from dataframe
A = list(df["actor"].unique())
B = list(df["movie_or_TV_name"].unique())
node_list = set(A+B)


# Create app layout
app.layout = html.Div([
    # Button to navigate to home page
    dcc.Link(html.Button('Home'), href='/', refresh=True),
    html.H1("Network Analysis with Dash", style={'text-align': 'center'}),
    # Create slider
    dcc.Slider(
        id='my-slider',
        min=0,
        max=100,
        step=1,
        value=50,
    ),
    html.Div(id='slider-output-container', children=[]),
    html.Br(),
    dcc.Graph(id='network_graph', figure={})
])

# Connect the Plotly graph with Dash Components
@app.callback(
    [Output(component_id='slider-output-container', component_property='children'),
     Output(component_id='network_graph', component_property='figure')],
    [Input(component_id='my-slider', component_property='value')]
)

# Function to update graph output
def update_graph(option_slctd):
    # Print integer selected by slider
    print(option_slctd)
    print(type(option_slctd))
    container = "Minimum number of shared actors is: {}".format(option_slctd)

    # Instatiate graph
    G = nx.Graph()

    # Add nodes from node list
    for i in node_list:
        G.add_node(i)

    # Add edges between nodes
    for i,j in df.iterrows():
        G.add_edges_from([(j["actor"],j["movie_or_TV_name"])])

    # Remove nodes that don't satisfy integer condition set by slider
    to_be_removed = [x for  x in G.nodes() if G.degree(x) <= option_slctd]
    for x in to_be_removed:
        G.remove_node(x)

    # Establish graph layout and node positions
    pos = nx.spring_layout(G, k=1.0, iterations=50)

    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')

    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    node_trace = go.Scatter(
        x=[],
        y=[],
        text=[],
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='RdBu',
            reversescale=True,
            color=[],
            size=15,
            colorbar=dict(
                thickness=10,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line=dict(width=0)))

    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color']+=tuple([len(adjacencies[1])])
        node_info = adjacencies[0] +' # of connections: '+str(len(adjacencies[1]))
        node_trace['text']+=tuple([node_info])

    # Plotly Express graph
    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Naruto Network Connections based on Voice Actors',
                    title_x = 0.5,
                    titlefont=dict(size=22),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="By Renzo and Zach",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))

    return container, fig


# Run App
if __name__ == '__main__':
    app.run_server(debug=True)

