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
                        html.Br(),
                        html.P('Para a confecção dos gráficos apresentados, foram utilizadas bases de dados confiáveis com as informações referentes à pandemia do novo coronavirus em âmbito mundial e nacional (Brasil), os datasets utilizados são de livre acesso e rigorosamente checados para trazer a máxima transparência para o usuário.', 
                            id='text_referencias_1',
                        ),
                    ],
                ),
                html.Div(
                    id='referencias_text_block_2',
                    children=[
                        html.Br(),
                        html.P('dlkhkjghkjaasasasddsdsddsdsdsdcceccececec', 
                            id='text_referencias_2',
                        ),
                    ],
                ),
                html.Div(
                    id='referencias_text_block_3',
                    children=[
                        html.Br(),
                        html.P('fhfjkfkfjhfjfhkjfhfkjfkjhfkjrhkjfhrjkhfjkoqooqoqoqoqoqooqoq',
                            id='text_referencias_3',
                        ),
                    ],
                ),
            ],
        )
    ],
)