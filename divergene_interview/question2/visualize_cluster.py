import dash
from dash import dcc
from dash import html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Dash Cytoscape:"),
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {'data': {'id': '1', 'label': 'GTTCCGGACCAGCGTCCGAAA'}},
{'data': {'id': '2', 'label': 'GTTCCGAACCAGCGTCCGAAA'}},
{'data': {'id': '3', 'label': 'GTTCCGGACCAGCGTCCGAAT'}},
{'data': {'id': '4', 'label': 'ATTCCGGACCAGCGTCCGAAA'}},
{'data': {'id': '5', 'label': 'GTTCCGGACCAGTGTCCGAAA'}},
{'data': {'source': '1', 'target': '2'}},
{'data': {'source': '1', 'target': '3'}},
{'data': {'source': '1', 'target': '4'}},
{'data': {'source': '1', 'target': '5'}}
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '1000px', 'height': '1000px'}
    )
])

app.run_server(port=5002, debug=True)
