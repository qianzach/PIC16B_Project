import pandas as pd
import plotly.graph_objects as go
import networkx as nx
import string

def create_graph(csv, min_connections):
    """
    create_graph() is the function that enables us to generate the network visualization. 

    our inputs are min_connections, which is an int that the user will input on the dash interface

    csv is the file name, which we use to load our data more autonomously

    we create a directed graph, compute centrality, and then add the parameters and custom colors, legend, etc we return the traces of the nodes and edges, which is used then in dash functionality

    This function serves as a more streamlined way to generate figures based on the work we did in a jupyter notebook made into a function from our previous collaborations on local jupyter notebooks

    """

    # Import data
    url = 'dash_package/web_scraper/{}.csv'.format(csv)
    df = pd.read_csv(url)

    # Instatiate graph
    G = nx.Graph()

    # Create nodelist from dataframe
    A = list(df["actor"].unique())
    B = list(df["movie_or_TV_name"].unique())
    node_list = set(A+B)

    # Add nodes from node list
    for i in node_list:
        G.add_node(i)

    # Add edges between nodes
    for i,j in df.iterrows():
        G.add_edges_from([(j["actor"],j["movie_or_TV_name"])])

    # Remove nodes that don't satisfy integer condition set by slider
    to_be_removed = [x for  x in G.nodes() if G.degree(x) <= min_connections]
    for x in to_be_removed:
        G.remove_node(x)

    # Establish graph layout and node positions
    pos = nx.spring_layout(G, k=1.0, iterations=50)

    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    #init trace of edge plot
    edge_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=0.5,color='#888'),
        hoverinfo='none',
        mode='lines')

    #Put in cartesian graph
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_trace['x'] += tuple([x0, x1, None])
        edge_trace['y'] += tuple([y0, y1, None])

    #init trace of node plot
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
            
    #put in cartesian graph
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])

    for node, adjacencies in enumerate(G.adjacency()):
        node_trace['marker']['color']+=tuple([len(adjacencies[1])])
        node_info = adjacencies[0] +' # of connections: '+str(len(adjacencies[1]) + min_connections)
        node_trace['text']+=tuple([node_info])


    return edge_trace, node_trace