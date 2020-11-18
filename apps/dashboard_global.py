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
import numpy as np

from app import app

#Definindo dataframe
#Definição do caminho para o dataset necessário e em seguida a leitura dele
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_global = pd.read_excel(DATA_PATH.joinpath("covid_global_trans.xlsx"))

#Fonte Original Do código do joao paulo
#df_global_top3 = df_global[['location','date','total_deaths']].sort_values( by=['date','total_deaths'],ascending=False).drop(45580, axis=0).dropna().head(3)

layout = html.Div(children=[
    html.Div(
        id='pop_up_global_message', #Div utilizada para avisar usuários de seleções que não são permitidas
        children=[
            html.H1('Aviso!',
                id='title_global_pop_up',
            ),
            html.P(' ',
                id='text_global_pop_up',
            ),
        ],
        hidden=True, #Até ser alterada para False essa div não é plotada
    ),
    html.Div(
        id='block_1',
        children=[
            html.Div( #Div inserida dentro da secção de filtros, para lidar com o texto "O que deseja ver?"
                id='seccao_filtros',
                children=[
                    html.Div(
                        id = "oq_deseja_ver", #Texto o que deseja ver?
                        children=[
                            html.P('O que deseja ver ?'), #Como o usuário verá
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 1"
                        id="grafico_1_filtro_text",
                        children=[
                            html.P('Gráfico 1'), #Como o usuário verá
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 2"
                        id="grafico_2_filtro_text",
                        children=[
                            html.P('Gráfico 2'), #Como o usuário verá
                        ]
                    ),
                    
                    html.Div(
                        id='Primeira_linha',
                        children=[
                            dcc.Dropdown(id = 'pais_grafico_1',
                                options = [{'label': i, 'value': i} for i in np.sort(df_global.location.unique())], 

                                optionHeight = 35,            #Espaço entre as opções do dropdown
                                value  = 'Mundo',             #Opção padrão ao iniciar a página
                                disabled = False,             #Capacidade de interagir com o dropdown
                                multi = False,                #Permitir múltiplas escolhas 
                                searchable = True,            #Permitir digitar para procurar valor
                                placeholder = 'Selecione...', #Frase que aparece quando nada foi selecionado
                                clearable = True,             #Permitir que seja apagado o valor escolhido
                                    #classname = '',               #Extrai a calsse de algum documento css dentro da pasata assets
                                persistence = True,           #Mantem o valor até que , no type memory, a página dê um refresh
                                persistence_type = 'memory',
                                style={
                                    'margin-top':'22px',
                                },
                            ),

                            dcc.Dropdown(id = 'pais_grafico_2', #Antes grafico2_dado1
                                options = [{'label': i, 'value': i} for i in np.sort(df_global.location.unique())], 
                                #options: Leitura da coluna location da planilha, para evitar repetição o unique
                                optionHeight = 35,
                                value  = 'Mundo',
                                disabled = False,
                                multi = False,                
                                searchable = True,
                                placeholder = 'Selecione...',
                                clearable = True,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                    'margin-top':'22px',
                                },
                            ),      
                        ],
                    ),

                    html.Div(
                        id='Segunda_linha',
                        children=[
                            dcc.Dropdown(id = 'casos_mortes_grafico_1',
                                options = [
                                    {'label': 'Casos', 'value':'grafico_casos' },
                                    {'label': 'Mortes', 'value': 'grafico_mortes'}], 

                                optionHeight = 35,
                                value  = ['grafico_casos', 'grafico_mortes'],
                                disabled = False,
                                multi = True,
                                searchable = False,
                                placeholder = 'Selecione...',
                                clearable = False,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                    'margin-top':'10px',
                                    'font-size':'15px',
                                },
                            ),

                            dcc.Dropdown(id = 'casos_mortes_grafico_2', 
                                options = [
                                    {'label': 'Casos', 'value':'grafico_casos' },
                                    {'label': 'Mortes', 'value': 'grafico_mortes'}], 

                                optionHeight = 35,
                                value  = ['grafico_casos', 'grafico_mortes'],
                                disabled = False,
                                multi = True,                
                                searchable = False,
                                placeholder = 'Selecione...',
                                clearable = False,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                    'margin-top':'10px',
                                    'font-size':'15px',
                                },
                            ),
                        ],
                    ),
                    
                    html.Div(
                        id='terceira_linha',
                        children=[
                            dcc.Dropdown(id = 'tipo_grafico_1',
                                options = [
                                    {'label': 'Barra', 'value':'grafico_barra' },
                                    {'label': 'Linha', 'value': 'grafico_linha'},
                                    {'label': 'Mapa', 'value': 'grafico_mapa'}
                                ], 

                                optionHeight = 35,
                                value  = 'grafico_barra',
                                disabled = False, 
                                multi = False,
                                searchable = False,
                                placeholder = 'Selecione...',
                                clearable = False,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                'margin-top':'10px',
                                },
                            ),

                            dcc.Dropdown(id = 'tipo_grafico_2',
                                options = [
                                    {'label': 'Barra', 'value':'grafico_barra' },
                                    {'label': 'Linha', 'value': 'grafico_linha'},
                                    {'label': 'Mapa', 'value': 'grafico_mapa'}
                                ], 

                                optionHeight = 35,
                                value  = 'grafico_barra',
                                disabled = False, 
                                multi = False,
                                searchable = False,
                                placeholder = 'Selecione...',
                                clearable = False,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                'margin-top':'10px',
                                },
                            ),
                        ],
                    ),
                    
                    html.Div(
                        id='filtros_gerais_text',
                        children=[
                            html.P('Filtros Gerais'),
                        ],
                    ),

                    html.Div(
                        id='Quarta_linha', 
                        style={
                            'fontSize':'1px',
                        },
                        children=[
                            dcc.DatePickerRange(
                                id='escolha_data',
                                min_date_allowed=date(2020, 1, 1),
                                max_date_allowed=date(2020, 12, 24),
                                #initial_visible_month=date(2020, 3, 10),
                                start_date=date(2020, 2, 14),
                                end_date=date(2020, 6, 20),
                            ),
    
                            html.Div(id='output-container-date-picker-range'),
                        ],
                    ),
                    html.Div(
                        children=[
                            html.Button(
                                'GO!',
                                id='Submit_button',
                                n_clicks=0,
                            ),
                        ],
                    ),
                ],
            ),

            html.Div(
                id='top_3',
                children=[
                    dcc.Graph(
                        id='top3_global',
                        config={
                            'displayModeBar': False,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': [
                                'zoom2d', 'pan2d', 'lasso2d', 'select2d', 'zoomIn2d', 'zoomOut2d',
                                'toggleSpikelines',
                            ],
                        },
                        style = {'border-radius': 30,},
                    ),
                ],
            ),
        ]
    ),

    html.Div( #Bloco de divs da direita --> Resumo geral, grafico 1 e grafico 2.
        className='resumo_geral',
        children=[
            html.Div(
                id='resumo_casos',
                children=[
                    html.Div(
                        id='icon_circle_casos',
                    ),

                    html.Img(
                        id='icon_casos',
                        src='/assets/icon_casos.svg',
                    ),

                    html.P(
                        'Casos Confirmados',
                        id='casos_confirmados_text',
                    ),

                    html.P(
                        'Acumulado',
                        id='acumulado_casos_text',
                    ),

                    html.P(
                        'Novos Casos',
                        id='novos_casos_text',
                    ),
                ],
            ),
            html.Div(
                id='colocar_algo',
            ),
            html.Div(
                id='resumo_obitos',
                children=[
                    html.Div(
                        id='icon_circle_obitos',
                    ),

                    html.Img(
                        id='icon_obitos',
                        src='/assets/icon_deaths.svg',
                    ),

                    html.P(
                        'Óbitos Confirmados',
                        id='obitos_confirmados',
                    ),

                    html.P(
                        'Acumulado',
                        id='acumulado_obitos_text',
                    ),

                    html.P(
                        'Letalidade',
                        id='letalidade_text',
                    ),

                    html.P(
                        'Novos Óbitos',
                        id='novos_obitos_text'
                    ),
                ],
            ),

            html.Div(
                id='grafico_1',
                children=[
                    dcc.Graph(
                        id='grafico-1',
                        config={
                            'displaylogo': False,
                            'modeBarButtonsToRemove':[
                                'lasso2d', 'select2d', 'zoomIn2d', 'zoomOut2d',
                                'toggleSpikelines',
                            ],
                        }, 
                    ),
                ],
            ),

            html.Div(
                id='grafico_2',
                children=[
                    dcc.Graph(
                        id='grafico-2',
                        config={
                            'displaylogo': False,
                            'modeBarButtonsToRemove':[
                                'lasso2d', 'select2d', 'zoomIn2d', 'zoomOut2d',
                                'toggleSpikelines',
                            ],
                        }, 
                    ),
                ],
            ),
        ],
    ),

])
@app.callback(
Output('grafico-1', 'figure'),
Input('Submit_button', 'n_clicks'), 
[State('pais_grafico_1', 'value'),
State('casos_mortes_grafico_1', 'value'),
State('escolha_data', 'start_date'),
State('escolha_data', 'end_date'),
State('tipo_grafico_1', 'value'),]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure(confirm_action, selected_location, selected_info, start_date, end_date, selected_graph):
    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')

    #Restrição do dataframe
    newlocation_df1 = df_global[df_global.location == selected_location]
    new_end_date_df1 = df_global[df_global.date == end_date_string]

    #Se a opção de tipo de informação ou tipo de localização estiver vazia, impedir atualização do gráfico 1
    if not selected_info or not selected_location: 
        raise PreventUpdate

    elif selected_graph == "grafico_barra":
        
        if selected_info == ['grafico_casos'] :

            fig_bar_global_1 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_cases'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 220, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_1.update_layout(
                title={
                    'text':'Gráfico de barras casos global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_bar_global_1  #devolvendo os gráficos que o usuario pediu no imput

        elif selected_info == ['grafico_mortes'] :
            fig_bar_global_1 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_deaths'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 72, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_1.update_layout(
                title={
                    'text':'Gráfico de barras mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_bar_global_1 #devolvendo os gráficos que o usuario pediu no imput

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_bar_global_1 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_cases'], 
                    x = newlocation_df1['date'],
                    marker =  dict(
                        autocolorscale = True,
                        color = 'rgb(255, 220, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ),
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>",  
                ),
                go.Bar(
                    y = newlocation_df1['total_deaths'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 72, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_1.update_layout(
                title={
                    'text':'Gráfico de barras casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_bar_global_1 #devolvendo os gráficos que o usuario pediu no imput
    
    elif selected_graph == "grafico_linha":
        
        if selected_info == ['grafico_casos']:
            fig_scatter_global_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"],    
                    y = newlocation_df1["total_cases"],
                    line = dict(
                        color = "rgb(255, 220, 0)",
                        width = 4,
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_1.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_scatter_global_1
        
        elif selected_info == ['grafico_mortes']:
            fig_scatter_global_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"], 
                    y = newlocation_df1["total_deaths"],
                    line = dict(
                        color = "rgb(255, 72, 0)",
                        width = 4,
                    ),
                    mode = "lines",
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_1.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_scatter_global_1

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_scatter_global_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"],    
                    y = newlocation_df1["total_cases"],
                    line = dict(
                        color = "rgb(255, 220, 0)",
                        width = 4,
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),

                go.Scatter(
                    x = newlocation_df1["date"], 
                    y = newlocation_df1["total_deaths"],
                    line = dict(
                        color = "rgb(255, 72, 0)",
                        width = 4,
                    ),
                    mode = "lines",
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_1.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_scatter_global_1

    elif selected_graph == "grafico_mapa":

        if selected_info == ['grafico_casos']:
            fig_map_global_1 = go.Figure(data=go.Choropleth(
                locations = new_end_date_df1['iso_code'],
                z =  new_end_date_df1['total_cases'],  
                zmax = 8000000,
                zmin = 0,
                text = new_end_date_df1['location'],
                colorscale = [[0, 'rgb(255, 250, 173)'], [1, 'rgb(255,220,0)']],
                autocolorscale = False,
                reversescale = False,
                marker_line_color = 'black',
                marker_line_width = 0.5,
                colorbar = dict(
                    bordercolor = "black",
                    borderwidth = 1,
                    tickprefix = '',
                    x = 0.8,
                ),
                hoverlabel = dict(
                    bgcolor = '#C5D5FD',
                    bordercolor = 'black',
                    font = dict(
                        family = 'Courier New',
                        color = 'black',
                    ),
                ),
                hovertemplate = " Data: %{text_2} <br> País: %{text} <br> Casos: %{z} <extra></extra>",  
                #Modificar data dps     
            ))

            fig_map_global_1.update_layout(
                geo = dict(
                    showframe=False,
                    showcoastlines=False,
                    projection_type='natural earth',
                    bgcolor = "#C5D5FD",
                ),
                title={
                    'text':'Gráfico de mapa de casos global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",    
            ),

            return fig_map_global_1

        elif selected_info == ['grafico_mortes']:
            fig_map_global_1 = go.Figure(data=go.Choropleth(
                locations = new_end_date_df1['iso_code'], 
                z =  new_end_date_df1['total_deaths'],  
                zmax = 300000,
                zmin = 0,
                text = new_end_date_df1['location'],
                colorscale = [[0, 'rgb(250, 127, 114)'], [1, 'rgb(139, 0, 0)']],
                autocolorscale = False,
                reversescale = False,
                marker_line_color = 'black',
                marker_line_width = 0.5,
                colorbar = dict(
                    bordercolor = "black",
                    borderwidth = 1,
                    tickprefix = '',
                    x = 0.8,
                ),
                hoverlabel = dict(
                    bgcolor = '#C5D5FD',
                    bordercolor = 'black',
                    font = dict(
                        family = 'Courier New',
                        color = 'black',
                    ),
                ),
                hovertemplate = " Data: 23 Set 2020 <br> País: %{text} <br> Mortes: %{z} <extra></extra>",  
                #Modificar data dps  
            ))

            fig_map_global_1.update_layout(
                title_text = 'Mortes por COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                ),
                title={
                    'text':'Gráfico de mapa de mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",    
            ),

            return fig_map_global_1
        
        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            raise PreventUpdate

#Analisar questão de inserir data limite no mapa
#Inserir button de confirmação 


#EM PROCESSO DE TESTE DE INTEGRAÇÃO DE DATA NO GRÁFICO
@app.callback(
Output('grafico-2', 'figure'),
Input('Submit_button', 'n_clicks'), 
[State('pais_grafico_2', 'value'),
State('casos_mortes_grafico_2', 'value'),
State('escolha_data', 'start_date'),
State('escolha_data', 'end_date'),
State('tipo_grafico_2', 'value'),]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure_2(confirm_action, selected_location, selected_info, start_date, 
                    end_date, selected_graph):

    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')
    newlocation_df1 = df_global[df_global.location == selected_location] #redefinindo o dataframe
    new_end_date_df1 = df_global[df_global.date == end_date_string]
    if not selected_info or not selected_location:
        raise PreventUpdate

    elif selected_graph == "grafico_barra":
        
        if selected_info == ['grafico_casos'] :

            fig_bar_global_2 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_cases'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 220, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_2.update_layout(
                title={
                    'text':'Gráfico de barras casos global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_bar_global_2  #devolvendo os gráficos que o usuario pediu no imput

        elif selected_info == ['grafico_mortes'] :
            fig_bar_global_2 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_deaths'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 72, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_2.update_layout(
                title={
                    'text':'Gráfico de barras mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_bar_global_2 #devolvendo os gráficos que o usuario pediu no imput

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_bar_global_2 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['total_cases'], 
                    x = newlocation_df1['date'],
                    marker =  dict(
                        autocolorscale = True,
                        color = 'rgb(255, 220, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ),
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>",  
                ),
                go.Bar(
                    y = newlocation_df1['total_deaths'],
                    x = newlocation_df1['date'],
                    marker = dict(
                        autocolorscale = True,
                        color = 'rgb(255, 72, 0)',
                        line = dict(
                            color = 'black',
                            width = 1,
                        ), 
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_bar_global_2.update_layout(
                title={
                    'text':'Gráfico de barras casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_bar_global_2 #devolvendo os gráficos que o usuario pediu no imput
    
    elif selected_graph == "grafico_linha":
        
        if selected_info == ['grafico_casos']:
            fig_scatter_global_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"],    
                    y = newlocation_df1["total_cases"],
                    line = dict(
                        color = "rgb(255, 220, 0)",
                        width = 4,
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_2.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ), 

            return fig_scatter_global_2
        
        elif selected_info == ['grafico_mortes']:
            fig_scatter_global_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"], 
                    y = newlocation_df1["total_deaths"],
                    line = dict(
                        color = "rgb(255, 72, 0)",
                        width = 4,
                    ),
                    mode = "lines",
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_2.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_scatter_global_2

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_scatter_global_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["date"],    
                    y = newlocation_df1["total_cases"],
                    line = dict(
                        color = "rgb(255, 220, 0)",
                        width = 4,
                    ),
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Casos: %{y} <extra></extra>", 
                ),

                go.Scatter(
                    x = newlocation_df1["date"], 
                    y = newlocation_df1["total_deaths"],
                    line = dict(
                        color = "rgb(255, 72, 0)",
                        width = 4,
                    ),
                    mode = "lines",
                    hoverlabel = dict(
                        bgcolor = '#C5D5FD',
                        bordercolor = 'black',
                        font = dict(
                            family = 'Courier New',
                            color = 'black',
                        ),
                    ),
                    hovertemplate = " Data: %{x} <br> Óbitos: %{y} <extra></extra>", 
                ),
            ])

            fig_scatter_global_2.update_layout(
                title={
                    'text':'Gráfico de linhas casos e mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",
            ),

            return fig_scatter_global_2

    elif selected_graph == "grafico_mapa":

        if selected_info == ['grafico_casos']:
            fig_map_global_2 = go.Figure(data=go.Choropleth(
                locations = new_end_date_df1['iso_code'],
                z =  new_end_date_df1['total_cases'],  
                zmax = 8000000,
                zmin = 0,
                text = new_end_date_df1['location'],
                colorscale = [[0, 'rgb(255, 250, 173)'], [1, 'rgb(255,220,0)']],
                autocolorscale = False,
                reversescale = False,
                marker_line_color = 'black',
                marker_line_width = 0.5,
                colorbar = dict(
                    bordercolor = "black",
                    borderwidth = 1,
                    tickprefix = '',
                    x = 0.8,
                ),
                hoverlabel = dict(
                    bgcolor = '#C5D5FD',
                    bordercolor = 'black',
                    font = dict(
                        family = 'Courier New',
                        color = 'black',
                    ),
                ),
                hovertemplate = " Data: %{text_2} <br> País: %{text} <br> Casos: %{z} <extra></extra>",  
                #Modificar data dps     
            ))

            fig_map_global_2.update_layout(
                geo = dict(
                    showframe=False,
                    showcoastlines=False,
                    projection_type='natural earth',
                    bgcolor = "#C5D5FD",
                ),
                title={
                    'text':'Gráfico de mapa de casos global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                barmode='overlay',
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",    
            ),

            return fig_map_global_2

        elif selected_info == ['grafico_mortes']:
            fig_map_global_2 = go.Figure(data=go.Choropleth(
                locations = new_end_date_df1['iso_code'], 
                z =  new_end_date_df1['total_deaths'],  
                zmax = 300000,
                zmin = 0,
                text = new_end_date_df1['location'],
                colorscale = [[0, 'rgb(250, 127, 114)'], [1, 'rgb(139, 0, 0)']],
                autocolorscale = False,
                reversescale = False,
                marker_line_color = 'black',
                marker_line_width = 0.5,
                colorbar = dict(
                    bordercolor = "black",
                    borderwidth = 1,
                    tickprefix = '',
                    x = 0.8,
                ),
                hoverlabel = dict(
                    bgcolor = '#C5D5FD',
                    bordercolor = 'black',
                    font = dict(
                        family = 'Courier New',
                        color = 'black',
                    ),
                ),
                hovertemplate = " Data: 23 Set 2020 <br> País: %{text} <br> Mortes: %{z} <extra></extra>",  
                #Modificar data dps  
            ))

            fig_map_global_2.update_layout(
                title_text = 'Mortes por COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                ),
                title={
                    'text':'Gráfico de mapa de mortes global',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-15,
                font_family="Courier New",
                font_size=12,
                margin=dict(
                    l=25,
                    r=25,
                    b=25,
                    t=45,  
                ),
                showlegend=False,
                plot_bgcolor = "#C5D5FD",    
            ),

            return fig_map_global_2

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            raise PreventUpdate

#Callback com erro por causa da data - Datas menores que 10.
@app.callback(
    Output('top3_global', 'figure'),
    Input('Submit_button', 'n_clicks'),
    State('escolha_data', 'end_date'),
)
def update_top_3_global(confirm_action, end_date):
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')
    new_end_date_df1 = df_global[df_global.date == end_date_string]
   
    df_global_top3 = new_end_date_df1[['location','total_deaths']].sort_values( by=['total_deaths'],ascending=False).query('location != "Mundo"').dropna().head(3)

    if not end_date:
        raise PreventUpdate

    else:
        fig_bar_global_top3 = go.Figure( data = [
            go.Bar(
                x= df_global_top3['location'], 
                y = df_global_top3['total_deaths'],
                textposition = 'auto',
                marker =  dict(
                    autocolorscale = True,
                    color = 'rgb(255, 72, 0)',
                    line = dict(
                        color = 'black',
                        width = 2,
                    ),
                ),        
                hoverlabel = dict(
                    bgcolor = '#C5D5FD',
                    bordercolor = 'black',
                    font = dict(
                        family = 'Courier New',
                        color = 'black',
                    ),
                ),
                hovertemplate = " País: %{x} <br> Óbitos: %{y} <extra></extra>", 
            ),
        ])
        fig_bar_global_top3.update_layout(
            title={
                'text':'Top 3',
                'font.size': 22,
                'x': 0.5,
                'y': 0.97,
            },
            xaxis_tickangle=-15,
            font_family="Courier New",
            font_size=12,
            margin=dict(
                l=25,
                r=25,
                b=10,
                t=45,  
            ),
            showlegend=False,
            plot_bgcolor = "#C5D5FD",
        ),

        return fig_bar_global_top3

#ERRO NO CALLBACK --> POP-UP ACONTECE MESMO QUANDO CONDIÇÃO NÃO SE APLICA.
#SITUAÇÃO 1 --> SELECIONAR MAPA TIPO CASO POP UP APARECE (NÃO DESEJADO)
#SITUAÇÃO 2 --> SELECIONA MAPA TIPO MORTE POP UP APARECE (NÃO DESEJADO)
#EM IMPLEMENTAÇÃO
'''
@app.callback(
    [Output('pop_up_global_message', 'hidden'),
    Output('text_global_pop_up', 'children')],
    Input('Submit_button', 'n_clicks'),
    [State('pais_grafico_1', 'value'),
    State('tipo_grafico_1', 'value'),
    State('casos_mortes_grafico_1', 'value'),
    State('pais_grafico_2', 'value'),
    State('tipo_grafico_2', 'value'),
    State('casos_mortes_grafico_2', 'value')]
)
def pop_up_message(confirm_action, selected_location, selected_graph, selected_info, 
                    selected_location_2, selected_graph_2, selected_info_2):

    if selected_graph_2 == "grafico_mapa" or selected_graph == "grafico_mapa":
        if ((selected_info_2 == ['grafico_casos', 'grafico_mortes'] or 
            ['grafico_mortes', 'grafico_casos']) or 
            (selected_info == ['grafico_casos', 'grafico_mortes'] or 
            ['grafico_mortes', 'grafico_casos'])):
            return False, 'O gráfico de mapa não pode receber as informações de morte e casos simultaneamente. Selecione casos ou mortes, ou altere o tipo de gráfico e tente novamente.'

    elif((not selected_location or not selected_location_2) and (not selected_info or not selected_info_2)):
        return False, 'Não é possível gerar gráficos com as opções localização e tipo de informação vazias. Selecione uma localização e um tipo de informação e tente novamente.' 
    
    elif (not selected_location or not selected_location_2):
        return False, 'Não é possível gerar gráficos com a opção localização vazia. Selecione uma localização e tente novamente.'

    elif (not selected_info or not selected_info_2):
        return False, 'Não é possível gerar gráficos com a opção tipo de informação vazia. Selecione casos, morte ou ambos e tente novamente.'

    else:
        return True, '...'

'''

@app.callback(
[Output('acumulado_casos_text', 'children'), 
Output('novos_casos_text', 'children'),
Output('acumulado_obitos_text', 'children'), 
Output('novos_obitos_text', 'children'), 
Output('letalidade_text', 'children')],
Input('Submit_button', 'n_clicks'),
[State('escolha_data', 'start_date'),
State('escolha_data', 'end_date'),]
)
def resumo_geral(confirm_action, start_date, end_date):
    
    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')

    newlocation_df1 = df_global[df_global['location'] == 'Mundo']
    data_resumo_geral_fim = newlocation_df1[newlocation_df1['date'] == end_date_string]
    data_resumo_geral_inicio = newlocation_df1[newlocation_df1['date'] == start_date_string]
    
    var_resumo_casos_fim  = float(data_resumo_geral_fim['total_cases'].values)
    var_resumo_casos_inicio = float(data_resumo_geral_inicio['total_cases'].values)
    var_resumo_mortes_fim  = float(data_resumo_geral_fim['total_deaths'].values)
    var_resumo_mortes_inicio = float(data_resumo_geral_inicio['total_deaths'].values)

    children_casos_acumulado =  'Acumulado: {}'.format(var_resumo_casos_fim)
    children_casos_novos = 'Novos casos: {}'.format(var_resumo_casos_fim - var_resumo_casos_inicio)
    children_mortes_acumulado = 'Acumulado: {}'.format(var_resumo_mortes_fim)
    children_mortes_novos = 'Novos óbitos: {}'.format(var_resumo_mortes_fim - var_resumo_mortes_inicio)
    children_letalidade = 'Letalidade: {:.2f}%'.format(var_resumo_mortes_fim*100/var_resumo_casos_fim)

    return [children_casos_acumulado, children_casos_novos, children_mortes_acumulado, children_mortes_novos, children_letalidade]
'''
        Esse código é uma tentativa de inserir o intervalo de data para gráfico de barra
        Funciona porém faltar melhorar

       start_date_object = date.fromisoformat(start_date)
        start_dia_string = start_date_object.strftime('%d')
        if(start_dia_string != "10" or start_dia_string != "20" or start_dia_string != "30"):
            start_dia_string = start_dia_string.replace("0", "")
        start_dia = int(start_dia_string)

        start_mes_string = start_date_object.strftime('%m')
        start_mes_string = start_mes_string.replace("0", "")
        start_mes = int(start_mes_string)

        start_ano_string = start_date_object.strftime('%Y')
        start_ano = int(start_ano_string)

        end_date_object = date.fromisoformat(end_date)
        end_dia_string = end_date_object.strftime('%d')
        if(end_dia_string != "10" or end_dia_string != "20" or end_dia_string != "30"):
            end_dia_string = end_dia_string.replace("0", "")
        end_dia = int(end_dia_string)

        end_mes_string = end_date_object.strftime('%m')
        end_mes_string = end_mes_string.replace("0", "")
        end_mes = int(end_mes_string)

        end_ano_string = end_date_object.strftime('%Y')
        end_ano = int(end_ano_string)
'''