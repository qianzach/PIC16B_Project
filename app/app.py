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
                    title='<br>Anime Network Connections based on Naruto: Shippuden Voice Actor List',
                    title_x = 0.5,
                    titlefont=dict(size=22),
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
    fig.update_yaxes(automargin=True)


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Interactive Network Graph"
    #export the csv
    return render_template('fig.html', header=header,graphJSON=graphJSON)

@app.route('/recommendations')
def recommendations():
    #load csv and output
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