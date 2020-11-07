import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import re
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import datetime
from datetime import date
import pathlib

from app import app

#Definindo dataframe
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_global = pd.read_excel(DATA_PATH.joinpath("covid_global.xlsx"))

layout = html.Div(children=[
    html.Img(
        src='../assets/logo_fga.png',
    ),    
])