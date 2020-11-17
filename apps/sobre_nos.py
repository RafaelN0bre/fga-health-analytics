import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

from app import app
 
layout = html.Div([
 
    html.Section(id="slideshow", children=[
        html.Div(id="slideshow-container", children=[
            html.Img(
                id="image",
                src='../assets/Card_Mauricio.png',
            ),
            dcc.Interval(id='interval', interval=3000)
        ])
    ])
 
])
 
@app.callback(Output('image', 'src'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 2 == 1:
        return '../assets/Card_Joao.png'
    elif n % 2 == 0:
        return '../assets/Card_Lavynia.png'
    else:
        return None