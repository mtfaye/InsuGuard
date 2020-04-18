import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from utils import data

app = dash.Dash(__name__)
app.title = 'Diabetes Monitoring App'
app.colors = {'background': '#5F5958'}

# Boostrap CSS
external_stylesheets = ['https://codepen.io/mtfaye/pen/MWgpoyp.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(children='kimaera-dynamics',
                        style={'color': 'white', 'fontSize': 23, 'text-indent': 10, 'line-height': 50},
                        className='banner'
                        )
            ], className="row"
        ),
        html.Div([
            html.Div(html.H5(
                children=""" About: """
            )
                , style={'textAlign': 'left'}),
            html.P("""Insuline and Glucose Monitoring""")
        ]),
        html.Div(children=[
            html.P('Select a channel - '),
            html.Div(
                [
                    html.P('Hackathon Together vs COVID19 - Developed by team kimaera-dynamics', style={'display': 'inline'}),
                    html.A('tahafaye@hotmail.com', href='mailto: tahafaye@hotmail.com')
                ], className="twelve columns",
                style={'fontSize': 14, 'padding-top': 18}
            )
        ], className="row")
    ], className='ten columns offset-by-one'
)


if __name__ == '__main__':
    app.run_server(debug=True)