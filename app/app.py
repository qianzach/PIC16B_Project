from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px

# For plotly network graph
import plotly.graph_objects as go
import networkx as nx



app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/networks')
def networks():
#    df = pd.DataFrame({
#       'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
#       'Amount': [4, 1, 2, 2, 4, 5],
#       'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
#    })
#    fig = px.bar(df, x='Fruit', y='Amount', color='City',    barmode='group')
   
    # Create random graph
    # G = nx.random_geometric_graph(200, 0.125)

    # # Create Edges
    # edge_x = []
    # edge_y = []
    # for edge in G.edges():
    #     x0, y0 = G.nodes[edge[0]]['pos']
    #     x1, y1 = G.nodes[edge[1]]['pos']
    #     edge_x.append(x0)
    #     edge_x.append(x1)
    #     edge_x.append(None)
    #     edge_y.append(y0)
    #     edge_y.append(y1)
    #     edge_y.append(None)

    # edge_trace = go.Scatter(
    #     x=edge_x, y=edge_y,
    #     line=dict(width=0.5, color='#888'),
    #     hoverinfo='none',
    #     mode='lines')

    # node_x = []
    # node_y = []
    # for node in G.nodes():
    #     x, y = G.nodes[node]['pos']
    #     node_x.append(x)
    #     node_y.append(y)

    # node_trace = go.Scatter(
    #     x=node_x, y=node_y,
    #     mode='markers',
    #     hoverinfo='text',
    #     marker=dict(
    #         showscale=True,
    #     # colorscale options
    #     #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
    #     #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
    #     #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
    #         colorscale='YlGnBu',
    #         reversescale=True,
    #         color=[],
    #         size=10,
    #         colorbar=dict(
    #             thickness=15,
    #             title='Node Connections',
    #             xanchor='left',
    #          titleside='right'
    #         ),
    #         line_width=2))

    # # Color Node Points
    # node_adjacencies = []
    # node_text = []
    # for node, adjacencies in enumerate(G.adjacency()):
    #     node_adjacencies.append(len(adjacencies[1]))
    #     node_text.append('# of connections: '+str(len(adjacencies[1])))

    # node_trace.marker.color = node_adjacencies
    # node_trace.text = node_text

    # # Create Graph
    # fig = go.Figure(data=[edge_trace, node_trace],
    #             layout=go.Layout(
    #                 title='<br>Network graph made with Python',
    #                 titlefont_size=16,
    #                 showlegend=False,
    #                 hovermode='closest',
    #                 margin=dict(b=20,l=5,r=5,t=40),
    #                 annotations=[ dict(
    #                     text="Insert Text",
    #                     showarrow=False,
    #                     xref="paper", yref="paper",
    #                     x=0.005, y=-0.002 ) ],
    #                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    #                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
    #                 )
    url = "../web_scraper/no_games.csv"
    df = pd.read_csv(url)

    A = list(df["actor"].unique())
    B = list(df["movie_or_TV_name"].unique())
    node_list = set(A+B)

    G = nx.Graph()

    for i in node_list:
        G.add_node(i)

    for i,j in df.iterrows():
        G.add_edges_from([(j["actor"],j["movie_or_TV_name"])])

    to_be_removed = [x for  x in G.nodes() if G.degree(x) <= 30]
    for x in to_be_removed:
        G.remove_node(x)
    
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
    

    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='<br>Naruto network connections',
                    titlefont=dict(size=16),
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=20,l=5,r=5,t=40),
                    annotations=[ dict(
                        text="Reference code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002) ],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Interactive Network Graph"
    return render_template('fig.html', header=header,graphJSON=graphJSON)

@app.route('/recommendations')
def recommendations():
    df = pd.DataFrame({
        "Vegetables": ["Lettuce", "Cauliflower", "Carrots", "Lettuce", "Cauliflower", "Carrots"],
        "Amount": [10, 15, 8, 5, 14, 25],
        "City": ["London", "London", "London", "Madrid", "Madrid", "Madrid"]
    })

    fig = px.bar(df, x="Vegetables", y="Amount", color="City", barmode="stack")

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Summary Page"
    description = """
    The rumor that vegetarians are having a hard time in London and Madrid can probably not be
    explained by this chart.
    """
    return render_template('fig.html', graphJSON=graphJSON, header=header,description=description)