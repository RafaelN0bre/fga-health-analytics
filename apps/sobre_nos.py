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
                src='../assets/Card_Davi.png',
            ),
            dcc.Interval(id='interval', interval= 5000)
        ])
    ])
 
])
 
@app.callback(Output('image', 'src'),
              [Input('interval', 'n_intervals')])
def display_image(n):
    if n == None or n % 10 == 9:
        return '../assets/Card_Rafael.png'
    elif n % 10 == 8:
        return '../assets/Card_Mauricio.png'
    elif n % 10 == 7:
        return '../assets/Card_Mateus.png'
    elif n % 10 == 6:
        return '../assets/Card_Marcos.png'
    elif n % 10 == 5:
        return '../assets/Card_Lavynia.png'
    elif n % 10 == 4:
        return '../assets/Card_Lara.png'
    elif n % 10 == 3:
        return '../assets/Card_Juan.png'
    elif n % 10 == 2:
        return '../assets/Card_JoaoPaulo.png'
    elif n % 10 == 1:
        return '../assets/Card_Joao.png'
    elif n % 10 == 0:
        return '../assets/Card_Davi.png'
    else:
        return None