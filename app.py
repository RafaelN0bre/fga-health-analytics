import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
import re
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
import datetime
from datetime import date


app = dash.Dash(__name__, title='Fga Health Analytics', update_title='Carregando...')
#Defindo Dataframe

df_global = pd.read_excel('covid_global.xlsx')

df_global_top3 = df_global[['location','date','total_deaths']].sort_values( by=['date','total_deaths'],ascending=False).drop(45580, axis=0).dropna().head(3)
data = [go.Bar(x =df_global_top3['location'], y=df_global_top3['total_deaths'] , textposition='auto', marker_color='red')]

conf_layout = go.Layout( 
    title={
        'text':'Top 3 Mortes',
        'x':0.5,
        'y':0.98,
        'font.size':30,
    },
    font_family="Courier New",
    font_size=14,
    margin=dict(
                l=25,
                r=25,
                b=25,
                t=40,
        ),
    )

fig_bar_global_top3 = go.Figure(data = data, layout=conf_layout)


app.layout = html.Div(children=[
    html.Div(
        id='header',
        children=[
            html.Img(
                id='logo_1',
                src='/assets/logo_fga.png',
            ),

            html.P(
                'FGA Health Analytics',
            ),

            html.Img(
                id='logo_2',
                src='/assets/logo_fga.png',
            ),
            html.Nav(
                id='navbar',

            ),
        ]
    ),
    
    html.Div(
        id='block_1',
        children=[
            html.Div( #Div inserida dentro da secção de filtros, para lidar com o texto "O que deseja ver?"
                id='seccao_filtros',
                children=[
                    html.Div(
                        id = "oq_deseja_ver", #id de referência para estilizaçao no css
                        children=[
                            html.P('O que deseja ver ?'), #texto inserido dentro do html.P
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 1"
                        id="grafico_1_filtro_text", #id para estilização no css
                        children=[
                            html.P('Gráfico 1'), # texto inserido dentro do html.P
                        ]
                    ),
                    html.Div( # Div inserida para colocar o texto "Gráfico 2"
                        id="grafico_2_filtro_text", #id para estilização no css
                        children=[
                            html.P('Gráfico 2'), # texto inserido dentro do html.P
                        ]
                    ),
                    
                    html.Div(
                        id='Primeira_linha',
                        children=[
                            dcc.Dropdown(id = 'pais_grafico_1', #antes escolha de pais
                                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 

                                optionHeight = 35,            #Espaço entre as opções do dropdown
                                value  = 'World',             #Opção padrão ao iniciar a página
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
                                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 
        
                                optionHeight = 35,
                                value  = 'World',
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
                            dcc.Dropdown(id = 'casos_mortes_grafico_1', #Antes casos_mortes
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
                                },
                            ),

                            dcc.Dropdown(id = 'casos_mortes_grafico_2', #Antes grafico2_dado2
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
                                },
                            ),
                        ],
                    ),
                    
                    html.Div(
                        id='terceira_linha',
                        children=[
                            dcc.Dropdown(id = 'grafico1_dado3',
                                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 

                                optionHeight = 35,
                                value  = 'World',
                                disabled = True, #Alterar esse valor para False quando for usar esse dropdown
                                multi = False,
                                searchable = True,
                                placeholder = 'Selecione...',
                                clearable = True,
                                persistence = True,
                                persistence_type = 'memory',
                                style={
                                'margin-top':'10px',
                                },
                            ),

                            dcc.Dropdown(id = 'grafico2_dado3', #Falta decidir o valor que será colocado nessa label.
                                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 

                                optionHeight = 35,
                                value  = 'World',
                                disabled = True, #Alterar esse valor para False quando for usar esse dropdown
                                multi = False,                
                                searchable = True,
                                placeholder = 'Selecione...',
                                clearable = True,
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
                                min_date_allowed=date(2020, 2, 1),
                                max_date_allowed=date(2020, 9, 24),
                                initial_visible_month=date(2020, 3, 10),
                                start_date=date(2020, 2, 1),
                                end_date=date(2020, 3, 15)
                            ),
    
                            html.Div(id='output-container-date-picker-range'),

                        ],
                    ),         
                ],
            ),

            html.Div(
                id='top_3',
                children=[
                    dcc.Graph(
                        id='top3_global',
                        figure = fig_bar_global_top3,
                        config={
                            'displayModeBar': False,
                            'displaylogo': False,
                            'modeBarButtonsToRemove': [
                                'zoom2d', 'pan2d', 'lasso2d', 'select2d', 'zoomIn2d', 'zoomOut2d',
                                'toggleSpikelines',
                            ],
                        },
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
                        id='grafico-1', #Antes example-graph
                        # figure=fig_bar_global - A figura será definida no callback.
                    ),
                ],
            ),

            html.Div(
                id='grafico_2',
                children=[
                    dcc.Graph(
                        id='grafico-2', #Antes example-graph_2
                        #figure=fig_bar_global_2 - A figura será definida no callback.
                    ),
                ],
            ),
        ],
    ),

])
@app.callback(
[Output('grafico-1', 'figure')],
[Input('pais_grafico_1', 'value'),
Input('casos_mortes_grafico_1', 'value')]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure(selected_location, selected_bars):
    newlocation_df1 = df_global[df_global.location == selected_location] #redefinindo o dataframe
    if not selected_bars or not selected_location:
        raise PreventUpdate

    elif selected_bars == ['grafico_casos']:
        fig_bar_global_1 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_cases'], name ='Casos', marker_color = "yellow"),
        ])
        fig_bar_global_1.update_layout(
            title_text='Gráfico 1 - Total de casos',
            title={'x':0.5, 'y':0.95,},
            xaxis_tickangle=-30,
            title_font_size=22,
            title_font_family='Courier New',
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
            showlegend=False,
        )
        
        return [fig_bar_global_1]  #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars == ['grafico_mortes']:
        fig_bar_global_1 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_deaths'], name ='Mortes', marker_color = "red"),
        ])
        fig_bar_global_1.update_layout(
            title_text='Gráfico 1 - Total de mortes',
            title={'x':0.5, 'y':0.95,},
            xaxis_tickangle=-30,
            title_font_size=22,
            title_font_family='Courier New',
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
                showlegend=False,
        ),
       
        return [fig_bar_global_1] #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']:
        fig_bar_global_1 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_cases'], name ='Casos', marker_color = "yellow"),
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_deaths'], name ='Mortes', marker_color = "red")
        ])
        fig_bar_global_1.update_layout(
            title_text='Gráfico 1 - Total de casos e mortes',
            title={'x':0.5, 'y':0.95,},
            title_font_size=22,
            title_font_family='Courier New',
            xaxis_tickangle=-30,
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
                showlegend=False,
        
        )
        
        return [fig_bar_global_1] #devolvendo os gráficos que o usuario pediu no imput
#EM PROCESSO DE TESTE DE INTEGRAÇÃO DE DATA NO GRÁFICO
@app.callback(
    [Output('grafico-2', 'figure'),],
    [Input('pais_grafico_2', 'value'),
    Input('casos_mortes_grafico_2', 'value'), 
    dash.dependencies.Input('escolha_data', 'start_date'),
    dash.dependencies.Input('escolha_data', 'end_date'),]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure2(selected_location2, selected_bars2, start_date, end_date):
    newlocation_df2 = df_global[df_global['location'] == selected_location2] #redefinindo o dataframe
    if not selected_bars2 or not selected_location2:
        raise PreventUpdate

    elif selected_bars2 == ['grafico_casos']:
        
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

        fig_bar_global_2 = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_cases'], name ='Casos', marker_color = "yellow"),
        ])
        fig_bar_global_2.update_layout(
            title_text='Gráfico 2 - Total de casos',
            title={'x':0.5, 'y':0.95,},
            xaxis_tickangle=-30,
            title_font_size=22,
            title_font_family='Courier New',
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
            showlegend=False,
            xaxis_range=[
                datetime.datetime(start_ano, start_mes, start_dia),
                datetime.datetime(end_ano, end_mes, end_dia)
            ]
        )

        return [fig_bar_global_2]  #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars2 == ['grafico_mortes']:
        
        fig_bar_global_2 = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_deaths'], name ='Mortes', marker_color = "red"),
        ])
        fig_bar_global_2.update_layout(
            title_text='Gráfico 2- Total de mortes',
            title={'x':0.5, 'y':0.95,},
            xaxis_tickangle=-30,
            title_font_size=22,
            title_font_family='Courier New',
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
                showlegend=False,
        )

        return [fig_bar_global_2]  #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars2 == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']:
       
        fig_bar_global_2 = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_cases'], name ='Casos', marker_color = "yellow"),
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_deaths'], name ='Mortes', marker_color = "red")
            ])
        fig_bar_global_2.update_layout(
            title_text='Gráfico 2 - Total de casos e mortes',
            title={'x':0.5, 'y':0.95,},
            xaxis_tickangle=-30,
            title_font_size=22,
            title_font_family='Courier New',
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=50,
            ),
                showlegend=False,
        )

        return [fig_bar_global_2]  #devolvendo os gráficos que o usuario pediu no imput

if __name__=="__main__":
    app.run_server(debug=True) 