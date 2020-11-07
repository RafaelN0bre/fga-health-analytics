import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app

layout = html.Div(
    children=[
        html.Div(
            id='logo_referencias_bloco',
            children=[
                html.Img(
                    id='logo_referencias_imagem',
                    src='../assets/book.svg',
                ),
            ],
        ),
        html.Div(
            id='section_referencias',
            children=[
                html.Div(
                    id='referencias_text_block_1',
                    children=[
                        html.P('djhdksjhdkjshdjkhdkjhdkjhdjkhfkjfhkjdhfkjhdjk'),
                    ],
                ),
                html.Div(
                    id='referencias_text_block_2',
                    children=[
                        html.P('dlkhkjghkjaasasasddsdsddsdsdsdcceccececec'),
                    ],
                ),
                html.Div(
                    id='referencias_text_block_3',
                    children=[
                        html.P('fhfjkfkfjhfjfhkjfhfkjfkjhfkjrhkjfhrjkhfjkoqooqoqoqoqoqooqoq'),
                    ],
                ),
            ],
        )
    ],
)