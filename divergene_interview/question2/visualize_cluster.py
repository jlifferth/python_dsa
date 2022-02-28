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
            {'data': {'id': 'ca', 'label': 'Canada'}},
            {'data': {'id': 'on', 'label': 'Ontario'}},
            {'data': {'id': 'qc', 'label': 'Quebec'}},
            {'data': {'source': 'ca', 'target': 'on'}},
            {'data': {'source': 'ca', 'target': 'qc'}}
        ],
        layout={'name': 'breadthfirst'},
        style={'width': '400px', 'height': '500px'}
    )
])

app.run_server(port=5002, debug=True)
