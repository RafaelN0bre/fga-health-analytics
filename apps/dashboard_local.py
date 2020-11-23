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
import json

from app import app

#Definindo dataframe
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df_local = pd.read_excel(DATA_PATH.joinpath("covid_brasil.xlsx"))


brazil_states = json.load(open('brazil-states.geojson', 'r'))

state_id_map = {}
for feature in brazil_states['features']:
    feature['id'] = feature['properties']['id']
    state_id_map[feature['properties']['sigla']] = feature['id']

layout = html.Div(children=[
    html.Div(
        id='pop_up_local_message', #Div utilizada para avisar usuários de seleções que não são permitidas
        children=[
            html.H1('Aviso!',
                id='title_local_pop_up',
            ),
            html.P(' ',
                id='text_local_pop_up',
            ),
        ],
        hidden=True, #Até ser alterada para False essa div não é plotada
    ),
    html.Div(
        id='block_1_local',
        children=[
            html.Div( #Div inserida dentro da secção de filtros, para lidar com o texto "O que deseja ver?"
                id='seccao_filtros_local',
                children=[
                    html.Div(
                        id = "oq_deseja_ver_local", #Texto o que deseja ver?
                        children=[
                            html.P('O que deseja ver ?'), #Como o usuário verá
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 1"
                        id="grafico_1_filtro_text_local",
                        children=[
                            html.P('Gráfico 1'), #Como o usuário verá
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 2"
                        id="grafico_2_filtro_text_local",
                        children=[
                            html.P('Gráfico 2'), #Como o usuário verá
                        ]
                    ),
                    
                    html.Div(
                        id='Primeira_linha_local',
                        children=[
                            dcc.Dropdown(id = 'pais_grafico_1_local',
                                options = [{'label': i, 'value': i} for i in np.sort(df_local['estado'].dropna().unique())], 

                                optionHeight = 35,            #Espaço entre as opções do dropdown
                                value  = 'RO',                #Opção padrão ao iniciar a página
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

                            dcc.Dropdown(id = 'pais_grafico_2_local', #Antes grafico2_dado1
                                options = [{'label': i, 'value': i} for i in np.sort(df_local['estado'].dropna().unique())], 
                                #options: Leitura da coluna location da planilha, para evitar repetição o unique
                                optionHeight = 35,
                                value  = 'PR',
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
                        id='Segunda_linha_local',
                        children=[
                            dcc.Dropdown(id = 'casos_mortes_grafico_1_local',
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

                            dcc.Dropdown(id = 'casos_mortes_grafico_2_local', 
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
                        id='terceira_linha_local',
                        children=[
                            dcc.Dropdown(id = 'tipo_grafico_1_local',
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

                            dcc.Dropdown(id = 'tipo_grafico_2_local',
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
                        id='filtros_gerais_text_local',
                        children=[
                            html.P('Filtros Gerais'),
                        ],
                    ),

                    html.Div(
                        id='Quarta_linha_local', 
                        style={
                            'fontSize':'1px',
                        },
                        children=[
                            dcc.DatePickerRange(
                                id='escolha_data_local',
                                min_date_allowed=date(2020, 1, 1),
                                max_date_allowed=date(2020, 12, 24),
                                #initial_visible_month=date(2020, 3, 10),
                                start_date=date(2020, 4, 20),
                                end_date=date(2020, 6, 20),
                            ),
    
                            html.Div(id='output-container-date-picker-range_local'),
                        ],
                    ),
                    html.Div(
                        children=[
                            html.Button(
                                'GO!',
                                id='Submit_button_local',
                                n_clicks=0,
                            ),
                        ],
                    ),
                ],
            ),

            html.Div(
                id='top_3_local',
                children=[
                    dcc.Graph(
                        id='top3_local',
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
        className='resumo_geral_local',
        children=[
            html.Div(
                id='resumo_casos_local',
                children=[
                    html.Div(
                        id='icon_circle_casos_local',
                    ),

                    html.Img(
                        id='icon_casos_local',
                        src='../assets/icone_casos.svg',
                    ),

                    html.P(
                        'Casos Confirmados',
                        id='casos_confirmados_text_local',
                    ),

                    html.P(
                        'Acumulado',
                        id='acumulado_casos_text_local',
                    ),

                    html.P(
                        'Novos Casos',
                        id='novos_casos_text_local',
                    ),
                ],
            ),
            html.Div(
                id='resumo_obitos_local',
                children=[
                    html.Div(
                        id='icon_circle_obitos_local',
                    ),

                    html.Img(
                        id='icon_obitos_local',
                        src='/assets/icon_deaths.svg',
                    ),

                    html.P(
                        'Óbitos Confirmados',
                        id='obitos_confirmados_local',
                    ),

                    html.P(
                        'Acumulado',
                        id='acumulado_obitos_text_local',
                    ),

                    html.P(
                        'Letalidade',
                        id='letalidade_text_local',
                    ),

                    html.P(
                        'Novos Óbitos',
                        id='novos_obitos_text_local'
                    ),
                ],
            ),

            html.Div(
                id='grafico_1_local',
                children=[
                    dcc.Graph(
                        id='grafico-1_local',
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
                id='grafico_2_local',
                children=[
                    dcc.Graph(
                        id='grafico-2_local',
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
Output('grafico-1_local', 'figure'),
Input('Submit_button_local', 'n_clicks'), 
[State('pais_grafico_1_local', 'value'),
State('casos_mortes_grafico_1_local', 'value'),
State('escolha_data_local', 'start_date'),
State('escolha_data_local', 'end_date'),
State('tipo_grafico_1_local', 'value'),]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure1_local(confirm_action, selected_location, selected_info, start_date, end_date, selected_graph):
    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')

    #Restrição do dataframe
    newlocation_df1 = df_local[df_local.estado == selected_location]
    new_end_date_df1 = df_local[df_local.data == end_date_string]
    dataframe_mapa_local = new_end_date_df1.dropna(subset = ['estado'])
    dataframe_mapa_local['id'] = dataframe_mapa_local['estado'].apply(lambda x: state_id_map[x])

    #Se a opção de tipo de informação ou tipo de localização estiver vazia, impedir atualização do gráfico 1
    if not selected_info or not selected_location: 
        raise PreventUpdate

    elif selected_graph == "grafico_barra":
        
        if selected_info == ['grafico_casos'] :

            fig_bar_local_1 = go.Figure( data = [go.Bar( 
                y = newlocation_df1['casosAcumulado'], 
                x = newlocation_df1['data'], 
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
            )])
            fig_bar_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_1  #devolvendo os gráficos que o usuario pediu no imput

        elif selected_info == ['grafico_mortes'] :
            
            fig_bar_local_1 = go.Figure( data = [go.Bar(
                y = newlocation_df1['obitosAcumulado'], 
                x = newlocation_df1['data'],
                marker =  dict(
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
            )])

            fig_bar_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_1 #devolvendo os gráficos que o usuario pediu no imput

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            
            fig_bar_local_1 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['casosAcumulado'], 
                    x = newlocation_df1['data'],
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
                    y = newlocation_df1['obitosAcumulado'],
                    x = newlocation_df1['data'],
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

            fig_bar_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_1

    
    elif selected_graph == "grafico_linha":
        
        if selected_info == ['grafico_casos']:
            
            fig_scatter_local_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"],    
                    y = newlocation_df1["casosAcumulado"],
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
            fig_scatter_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_1
        
        elif selected_info == ['grafico_mortes']:
            fig_scatter_local_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"], 
                    y = newlocation_df1["obitosAcumulado"],
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

            fig_scatter_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_1

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            
            fig_scatter_local_1 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"],    
                    y = newlocation_df1["casosAcumulado"],
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
                    x = df_local["data"], 
                    y = df_local["obitosAcumulado"],
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
            fig_scatter_local_1.update_layout(
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_1


    elif selected_graph == "grafico_mapa":

        if selected_info == ['grafico_casos']:
            fig_map_local_1 = go.Figure(data=go.Choropleth(
                locations = dataframe_mapa_local['id'], 
                z =  dataframe_mapa_local['casosAcumulado'],  
                zmax = 200000,
                zmin = 0,
                text = dataframe_mapa_local['estado'],
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
                geojson = brazil_states,
                hovertemplate = " Data: 24 Set 2020 <br> estado: %{text} <br> Casos: %{z} <extra></extra>",
            ))

            fig_map_local_1.update_geos(
                fitbounds = 'locations',
                visible=False,)

            fig_map_local_1.update_layout(
                title_text = 'Casos de COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                    scope = 'south america',
                ),
                title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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
            )


            return fig_map_local_1

        elif selected_info == ['grafico_mortes']:
            fig_map_local_1 = go.Figure(data=go.Choropleth(
                locations = dataframe_mapa_local['id'], 
                z =  dataframe_mapa_local['obitosAcumulado'],  
                zmax = 35000,
                zmin = 0,
                text = dataframe_mapa_local['estado'],
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
                geojson = brazil_states,
                hovertemplate = " Data: 23 Set 2020 <br> Estado: %{text} <br> Mortes: %{z} <extra></extra>",
            ))

            fig_map_local_1.update_geos(
                fitbounds = 'locations',
                visible=False,)

            fig_map_local_1.update_layout(
                title_text = 'Casos de COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                    scope = 'south america',
                ),
                 title={
                    'text':'Gráfico 1',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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
            )

            return fig_map_local_1
        
        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            raise PreventUpdate

#Analisar questão de inserir data limite no mapa
#Inserir button de confirmação 


#EM PROCESSO DE TESTE DE INTEGRAÇÃO DE DATA NO GRÁFICO
@app.callback(
Output('grafico-2_local', 'figure'),
Input('Submit_button_local', 'n_clicks'), 
[State('pais_grafico_2_local', 'value'),
State('casos_mortes_grafico_2_local', 'value'),
State('escolha_data_local', 'start_date'),
State('escolha_data_local', 'end_date'),
State('tipo_grafico_2_local', 'value'),]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure_2_local(confirm_action, selected_location, selected_info, start_date, 
                    end_date, selected_graph):

    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')
    newlocation_df1 = df_local[df_local.estado == selected_location] #redefinindo o dataframe
    new_end_date_df1 = df_local[df_local.data == end_date_string]
    dataframe_mapa_local = new_end_date_df1.dropna(subset = ['estado'])
    dataframe_mapa_local['id'] = dataframe_mapa_local['estado'].apply(lambda x: state_id_map[x])

    if not selected_info or not selected_location:
        raise PreventUpdate

    elif selected_graph == "grafico_barra":
        
        if selected_info == ['grafico_casos'] :

            fig_bar_local_2 = go.Figure( data = [go.Bar( 
                y = newlocation_df1['casosAcumulado'], 
                x = newlocation_df1['data'], 
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
            )])
            fig_bar_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_2  #devolvendo os gráficos que o usuario pediu no imput

        elif selected_info == ['grafico_mortes'] :
            fig_bar_local_2 = go.Figure( data = [go.Bar(
                y = newlocation_df1['obitosAcumulado'], 
                x = newlocation_df1['data'],
                marker =  dict(
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
            )])

            fig_bar_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_2 #devolvendo os gráficos que o usuario pediu no imput

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_bar_local_2 = go.Figure( data = [
                go.Bar(
                    y = newlocation_df1['casosAcumulado'], 
                    x = newlocation_df1['data'],
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
                    y = newlocation_df1['obitosAcumulado'],
                    x = newlocation_df1['data'],
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

            fig_bar_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_bar_local_2 #devolvendo os gráficos que o usuario pediu no imput
    
    elif selected_graph == "grafico_linha":
        
        if selected_info == ['grafico_casos']:
            fig_scatter_local_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"],    
                    y = newlocation_df1["casosAcumulado"],
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
            fig_scatter_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_2
        
        elif selected_info == ['grafico_mortes']:
            fig_scatter_local_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"], 
                    y = newlocation_df1["obitosAcumulado"],
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

            fig_scatter_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_2

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            fig_scatter_local_2 = go.Figure( data = [
                go.Scatter(
                    x = newlocation_df1["data"],    
                    y = newlocation_df1["casosAcumulado"],
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
                    x = df_local["data"], 
                    y = df_local["obitosAcumulado"],
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
            fig_scatter_local_2.update_layout(
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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

            return fig_scatter_local_2

    elif selected_graph == "grafico_mapa":

        if selected_info == ['grafico_casos']:
            fig_map_local_2 = go.Figure(data=go.Choropleth(
                locations = dataframe_mapa_local['id'], 
                z =  dataframe_mapa_local['casosAcumulado'],  
                zmax = 200000,
                zmin = 0,
                text = dataframe_mapa_local['estado'],
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
                geojson = brazil_states,
                hovertemplate = " Data: 24 Set 2020 <br> estado: %{text} <br> Casos: %{z} <extra></extra>",
            ))

            fig_map_local_2.update_geos(
                fitbounds = 'locations',
                visible=False,)

            fig_map_local_2.update_layout(
                title_text = 'Casos de COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                    scope = 'south america',
                ),
                title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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
            )


            return fig_map_local_2

        elif selected_info == ['grafico_mortes']:
            fig_map_local_2 = go.Figure(data=go.Choropleth(
                locations = dataframe_mapa_local['id'], 
                z =  dataframe_mapa_local['obitosAcumulado'],  
                zmax = 35000,
                zmin = 0,
                text = dataframe_mapa_local['estado'],
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
                geojson = brazil_states,
                hovertemplate = " Data: 23 Set 2020 <br> Estado: %{text} <br> Mortes: %{z} <extra></extra>",
            ))

            fig_map_local_2.update_geos(
                fitbounds = 'locations',
                visible=False,)

            fig_map_local_2.update_layout(
                title_text = 'Casos de COVID-19',
                geo = dict(
                    showframe = False,
                    showcoastlines = False,
                    projection_type = 'natural earth',
                    bgcolor = "#C5D5FD",
                    scope = 'south america',
                ),
                 title={
                    'text':'Gráfico 2',
                    'font.size': 22,
                    'x': 0.5,
                    'y': 0.97,
                },
                xaxis_tickangle=-30,
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
            )

            return fig_map_local_2

        elif (selected_info == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']):
            raise PreventUpdate

#Callback com erro por causa da data - Datas menores que 10.
@app.callback(
    Output('top3_local', 'figure'),
    Input('Submit_button_local', 'n_clicks'),
    State('escolha_data_local', 'end_date'),
)
def update_top_3_local(confirm_action, end_date):
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')
    new_end_date_df1 = df_local[df_local.data == end_date_string]
   
    df_local_top3 = new_end_date_df1[['estado','obitosAcumulado']].sort_values( by=['obitosAcumulado'],ascending=False).dropna().head(3)

    if not end_date:
        raise PreventUpdate

    else:
        fig_bar_local_top3 = go.Figure( data = [
            go.Bar(
                x= df_local_top3['estado'], 
                y = df_local_top3['obitosAcumulado'],
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
        fig_bar_local_top3.update_layout(
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

        return fig_bar_local_top3

@app.callback(
[Output('acumulado_casos_text_local', 'children'), 
Output('novos_casos_text_local', 'children'),
Output('acumulado_obitos_text_local', 'children'), 
Output('novos_obitos_text_local', 'children'), 
Output('letalidade_text_local', 'children')],
Input('Submit_button_local', 'n_clicks'),
[State('escolha_data_local', 'start_date'),
State('escolha_data_local', 'end_date'),]
)
def resumo_geral(confirm_action, start_date, end_date):
    
    start_date_object = date.fromisoformat(start_date)
    start_date_string = start_date_object.strftime('%d/%m/%Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_string = end_date_object.strftime('%d/%m/%Y')

    newlocation_df1 = df_local[df_local['regiao'] == 'Brasil']
    data_resumo_geral_fim = newlocation_df1[newlocation_df1['data'] == end_date_string]
    data_resumo_geral_inicio = newlocation_df1[newlocation_df1['data'] == start_date_string]
    
    var_resumo_casos_fim  = float(data_resumo_geral_fim['casosAcumulado'].values)
    var_resumo_casos_inicio = float(data_resumo_geral_inicio['casosAcumulado'].values)
    var_resumo_mortes_fim  = float(data_resumo_geral_fim['obitosAcumulado'].values)
    var_resumo_mortes_inicio = float(data_resumo_geral_inicio['obitosAcumulado'].values)

    children_casos_acumulado =  'Acumulado: {}'.format(var_resumo_casos_fim)
    children_casos_novos = 'Novos casos: {}'.format(var_resumo_casos_fim - var_resumo_casos_inicio)
    children_mortes_acumulado = 'Acumulado: {}'.format(var_resumo_mortes_fim)
    children_mortes_novos = 'Novos óbitos: {}'.format(var_resumo_mortes_fim - var_resumo_mortes_inicio)
    children_letalidade = 'Letalidade: {:.2f}%'.format(var_resumo_mortes_fim*100/var_resumo_casos_fim)

    return [children_casos_acumulado, children_casos_novos, children_mortes_acumulado, children_mortes_novos, children_letalidade]