import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from utils import dict_main

data = list(dict_main.keys())
channels = dict_main[data[0]]

app = dash.Dash(__name__)
app.title = 'InsuGuard App'
app.colors = {'background': '#5F5958'}

# Boostrap CSS
external_stylesheets = ['https://codepen.io/mtfaye/pen/MWgpoyp.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(children='Insuline Tracker App',
                        style={'color': 'white', 'fontSize': 23, 'text-indent': 10, 'line-height': 50},
                        className='banner'
                        )
            ], className="row"
        ),
        html.Div([
            html.Div(html.H5(
                children=""" About the app: """
            )
                , style={'textAlign': 'left'}),
            html.P(
                """This alpha version of the app collects data from 70 diabetes patient throughout a year using an 
                automatic electronic recording device connected to the patients. The app monitor the fluctuation of 
                glucose, insuline levels and also dose injection. Whenever the app stop receiving data from a 
                single patient it raises an alert and notify the medical staff for an immediate assistance. """
            ),
            html.Div([

        dbc.ListGroupItem("33 = Regular insulin dose"),
        dbc.ListGroupItem("65 = Hypoglycemic symptoms"),
        dbc.ListGroupItem("35 = UltraLente insulin dose"),
        dbc.ListGroupItem("72 = Unspecified special event"),
            ])

        ]),
        html.Div(children=[
            html.Div(
                [
                    dbc.Button("Warning", color="Red", outline=True, size="lg", className="mr-1"),
                    dbc.Button("Danger", color="Yellow", outline=True, size="lg", className="mr-1"),
                    dbc.Button("Info", color="info", outline=True, size="lg", className="mr-1")
                ]
            )
            ,
            html.Div([
                dcc.Graph(id='Main-Graph',
                          figure=go.Figure(
                              data=[go.Scatter(x=data, y=channels)]
                          )),
                html.Div([
                    dcc.Dropdown(
                        id='data-dropdown',
                        options=[{'label': label, 'value': label} for label in data],
                        value=list(dict_main.keys())[0],
                        multi=False,
                        searchable=False)],
                    style={'width': '33%', 'display': 'inline-block'}),
                html.Div([
                    dcc.Dropdown(
                        id='x-axis-dropdown',
                        multi=False)],
                    style={'width': '33%', 'display': 'inline-block'}),
                html.Div([
                    dcc.Dropdown(
                        id='y-axis-dropdown',
                        multi=False)],
                    style={'width': '33%', 'display': 'inline-block'})
            ]),
            html.Div(
                [
                    html.P('Developed by: ',
                           style={'display': 'inline'}),
                    html.A('InsuGuard', href='mailto: InsuGuard')
                ], className="twelve columns",
                style={'fontSize': 14, 'padding-top': 18}
            )
        ], className="row")
    ], className='ten columns offset-by-one'
)


@app.callback(
    dash.dependencies.Output('Main-Graph', 'figure'),
    [dash.dependencies.Input('data-dropdown', 'value'),
     dash.dependencies.Input('x-axis-dropdown', 'value'),
     dash.dependencies.Input('y-axis-dropdown', 'value')],
    [dash.dependencies.State('Main-Graph', 'figure')]
)
def updateGraph(df_name, x_field, y_field, data):
    source = data['data']
    df = dict_main[df_name]

    if x_field and y_field and x_field in df.columns and y_field in df.columns:
        new_source = [{'x': df[x_field].tolist(), 'y': df[y_field].tolist()}]
        source = new_source
    return {
        'data': source,
        'layout': data['layout']
    }


@app.callback(
    [dash.dependencies.Output('x-axis-dropdown', 'options'),
     dash.dependencies.Output('y-axis-dropdown', 'options')],
    [dash.dependencies.Input('data-dropdown', 'value')]
)
def update_date_dropdown(selected):
    if selected is None:
        return dict_main['data-01']
    fields = [{'label': i, 'value': i} for i in dict_main[selected]]
    return [fields, fields]


if __name__ == '__main__':
    app.run_server(debug=True)
