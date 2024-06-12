import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Load data
data = pd.read_csv('C:/Users/Alejandro/OneDrive/Desktop/Dissertation-Object-Search/Study 1/data/10322_VAST1_2023-11-01_14h13.15.208.csv')

# Get column names for dropdown options
dropdown_options = [{'label': col, 'value': col} for col in data.columns]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='My Dashboard'),
    dcc.Dropdown(
        id='dropdown',
        options=dropdown_options,
        value=dropdown_options[0]['value']  # Default value
    ),
    dcc.Graph(id='example-graph')
])

# Define callback to update graph
@app.callback(
    Output('example-graph', 'figure'),
    [Input('dropdown', 'value')]
)
def update_graph(selected_column):
    # Assuming 'salary' is always available in your data for y-axis
    fig = px.scatter(data, x=selected_column, y='salary', title=f'{selected_column} vs. Salary')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
