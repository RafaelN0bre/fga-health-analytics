import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate


app = dash.Dash(__name__, title='Fga Health Analytics', update_title='Carregando...')
#Defindo Dataframe
df_global = pd.read_excel('covid_global.xlsx')

#df_global = df_global[df_global['location']=='Afghanistan']

#Definindo Gráfico 1 (O gráfico 1 não será mais definido aqui, mas sim no callback)
# fig_bar_global = go.Figure( data = [
#     go.Bar(x = df_global[df_global['location']=='Afghanistan']['date'], y = df_global[df_global['location']=='Afghanistan']['total_cases'], name ='Casos', marker_color = "yellow"),
#     go.Bar(x = df_global[df_global['location']=='Afghanistan']['date'], y = df_global[df_global['location']=='Afghanistan']['total_deaths'], name ='Mortes', marker_color = "red"),
# ])
# fig_bar_global.update_layout(
#     barmode='overlay',
#     margin=dict(
#         l=25,
#         r=25,
#         b=25,
#         t=25,
#     ),
#     showlegend=False,
# )

#Definindo Gráfico 2 (O gráfico 2 não será mais definido aqui, mas sim no callback)
# fig_bar_global_2 = go.Figure( data = [
#     go.Bar(x = df_global[df_global['location']=='Afghanistan']['date'], y = df_global[df_global['location']=='Afghanistan']['total_cases'], name ='Casos', marker_color = "yellow"),
#     go.Bar(x = df_global[df_global['location']=='Afghanistan']['date'], y = df_global[df_global['location']=='Afghanistan']['total_deaths'], name ='Mortes', marker_color = "red"),
# ])
# fig_bar_global_2.update_layout(
#     barmode='overlay',
#     margin=dict(
#         l=25,
#         r=25,
#         b=25,
#         t=25,
#     ),
#     paper_bgcolor='#C5D5FD',
# )

app.layout = html.Div(children=[
    html.Div(
        id='header',
        children=[
            html.Img(
                id='logo_1',
                src='/assets/logo_fga.png',
            ),

            html.P('FGA Health Analytics'),

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
                    dcc.Dropdown(id = 'escolha_de_pais', #muda o local dod dois gráficos.
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
                    ),
                    dcc.Dropdown(id = 'casos_mortes', #Falta decidir o valor que será colocado nessa label.
                        options = [
                            {'label': 'Casos', 'value':'grafico_casos' },
                            {'label': 'Mortes', 'value': 'grafico_mortes'}], 

                        optionHeight = 35,
                        value  = ['grafico_casos', 'grafico_mortes'],
                        disabled = False,
                        multi = True,
                        searchable = False,
                        placeholder = 'Selecione...',
                        clearable = True,
                        persistence = True,
                        persistence_type = 'memory',
                    ),
                    dcc.Dropdown(id = 'grafico1_dado3',
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
                    ),

                    dcc.Dropdown(id = 'grafico2_dado1', #Falta decidir o valor que será colocado nessa label.
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
                    ),

                    dcc.Dropdown(id = 'grafico2_dado2', #Falta decidir o valor que será colocado nessa label.
                         options = [
                            {'label': 'Casos', 'value':'grafico_casos' },
                            {'label': 'Mortes', 'value': 'grafico_mortes'}], 

                        optionHeight = 35,
                        value  = ['grafico_casos', 'grafico_mortes'],
                        disabled = False,
                        multi = True,                
                        searchable = True,
                        placeholder = 'Selecione...',
                        clearable = True,
                        persistence = True,
                        persistence_type = 'memory',
                    ),

                    dcc.Dropdown(id = 'grafico2_dado3', #Falta decidir o valor que será colocado nessa label.
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
                    ),

                    html.Div(
                        id='filtros_gerais_text',
                        children=[
                            html.P('Filtros Gerais'),
                        ],
                    ),

                    dcc.Dropdown(id = 'dado_7', #Falta decidir o valor que será colocado nessa label.
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
                    ),

                    dcc.Dropdown(id = 'dado_8', #Falta decidir o valor que será colocado nessa label.
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
                    ),
                ]
            ),

            html.Div(
                id='top_3',
                children=[
                    
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
                        id='example-graph',
                        # figure=fig_bar_global - A figura será definida no callback.
                    ),
                ],
            ),

            html.Div(
                id='grafico_2',
                children=[
                    dcc.Graph(
                        id='example-graph_2',
                        #figure=fig_bar_global_2 - A figura será definida no callback.
                    ),
                ],
            ),
        ],
    ),

])
@app.callback(
[Output('example-graph_2', 'figure')],
[Input('escolha_de_pais', 'value'),
Input('casos_mortes', 'value')]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure(selected_location, selected_bars):
    newlocation_df1 = df_global[df_global.location == selected_location] #redefinindo o dataframe
    if not selected_bars:
        raise PreventUpdate

    elif selected_bars == ['grafico_casos']:
        fig_bar_global_2 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_cases'], name ='Casos', marker_color = "yellow"),
        ])
        fig_bar_global_2.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
            ),
            showlegend=False,
        
    )
        
        return [fig_bar_global_2]  #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars == ['grafico_mortes']:
        fig_bar_global_2 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_deaths'], name ='Mortes', marker_color = "red"),
        ])
        fig_bar_global_2.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
            ),
                showlegend=False,
        
        )
       
        return [fig_bar_global_2] #devolvendo os gráficos que o usuario pediu no imput

    if selected_bars == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']:
        fig_bar_global_2 = go.Figure( data = [    #arrumando o gráfico de acordo com o imput e o novo dataframe
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_cases'], name ='Casos', marker_color = "yellow"),
            go.Bar(x = newlocation_df1['date'], y = newlocation_df1['total_deaths'], name ='Mortes', marker_color = "red")
        ])
        fig_bar_global_2.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
            ),
                showlegend=False,
        
        )
        
        return [fig_bar_global_2] #devolvendo os gráficos que o usuario pediu no imput


@app.callback(
[Output('example-graph', 'figure'),],
[Input('grafico2_dado1', 'value'),
Input('grafico2_dado2', 'value')]) #primeiro o id do dropdown q será utilizado, dps a propriedade q será mudada.
def update_figure2(selected_location2, selected_bars2):
    newlocation_df2 = df_global[df_global['location'] == selected_location2] #redefinindo o dataframe
    if not selected_bars2:
        raise PreventUpdate

    elif selected_bars2 == ['grafico_casos']:
        
        fig_bar_global = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_cases'], name ='Casos', marker_color = "yellow"),
        ])
        fig_bar_global.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
        ),
            showlegend=False,
    )
        return [fig_bar_global]  #devolvendo os gráficos que o usuario pediu no imput

    elif selected_bars2 == ['grafico_mortes']:
        
        fig_bar_global = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_deaths'], name ='Mortes', marker_color = "red"),
        ])
        fig_bar_global.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
            ),
                showlegend=False,
        )
        return [fig_bar_global]  #devolvendo os gráficos que o usuario pediu no imput

    if selected_bars2 == ['grafico_casos', 'grafico_mortes'] or ['grafico_mortes', 'grafico_casos']:
       
        fig_bar_global = go.Figure( data = [
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_cases'], name ='Casos', marker_color = "yellow"),
            go.Bar(x = newlocation_df2['date'], y = newlocation_df2['total_deaths'], name ='Mortes', marker_color = "red")
            ])
        fig_bar_global.update_layout(
            barmode='overlay',
            margin=dict(
                l=25,
                r=25,
                b=25,
                t=25,
            ),
                showlegend=False,
        
        )
        return [fig_bar_global]  #devolvendo os gráficos que o usuario pediu no imput

if __name__=="__main__":
    app.run_server(debug=True) 