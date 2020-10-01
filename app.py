import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

app = dash.Dash(__name__, title='Fga Health Analytics', update_title='Carregando...')
#Defindo Dataframe
df_global = pd.read_excel('covid_global.xlsx')

df_global = df_global[df_global['location']=='Afghanistan']

#Definindo Gráfico 1 
fig_bar_global = go.Figure( data = [
    go.Bar(x = df_global['date'], y = df_global['total_cases'], name ='Casos', marker_color = "yellow"),
    go.Bar(x = df_global['date'], y = df_global['total_deaths'], name ='Mortes', marker_color = "red"),
])
fig_bar_global.update_layout(
    barmode='overlay',
    height=275,
    margin=dict(
        l=25,
        r=25,
        b=25,
        t=25,
    ),
)

#Definindo Gráfico 2
fig_bar_global_2 = go.Figure( data = [
    go.Bar(x = df_global['date'], y = df_global['total_cases'], name ='Casos', marker_color = "yellow"),
    go.Bar(x = df_global['date'], y = df_global['total_deaths'], name ='Mortes', marker_color = "red"),
])
fig_bar_global_2.update_layout(
    barmode='overlay',
    height=275,
    margin=dict(
        l=25,
        r=25,
        b=25,
        t=25,
    ),
)

app.layout = html.Div(children=[
    html.Div(
        id='header',
        children=[
            html.Img(
                src='/assets/logo_fga.png'
            ),

            html.P('FGA Health Analytics'),

            html.Img(
                src='/assets/logo_fga.png'
            ),
        ]
    ),
    
    html.Div(
        id='seccao_filtros',
        children=[
            dcc.Dropdown(id = 'escolha_de_pais',
                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 

                optionHeight = 35,            #Espaço entre as opções do dropdown
                value  = 'World',             #Opção padrão ao iniciar a página
                disabled = False,             #Capacidade de interagir com o dropdown
                multi = False,                #Permitir múltiplas escolhas 
                searchable = True,            #Permitir digitar para procurar valor
                placeholder = 'Selecione...', #Frase que aparece quando nada foi selecionado
                clearable = True,             #Permitir que seja apagado o valor escolhido
                style = {'width' : '200px', 'display' : 'inline-block'},    #Estilização
               #classname = '',               #Extrai a calsse de algum documento css dentro da pasata assets
                persistence = True,           #Mantem o valor até que , no type memory, a página dê um refresh
                persistence_type = 'memory',
            ),
            dcc.Dropdown(id = 'decidir_input', #Falta decidir o valor que será colocado nessa label.
                options = [{'label': i, 'value': i} for i in df_global.location.unique()], 

                optionHeight = 35,            #Espaço entre as opções do dropdown
                value  = 'World',             #Opção padrão ao iniciar a página
                disabled = False,             #Capacidade de interagir com o dropdown
                multi = False,                #Permitir múltiplas escolhas 
                searchable = True,            #Permitir digitar para procurar valor
                placeholder = 'Selecione...', #Frase que aparece quando nada foi selecionado
                clearable = True,             #Permitir que seja apagado o valor escolhido
                style = {'width' : '200px', 'display' : 'inline-block'},    #Estilização
               #classname = '',               #Extrai a calsse de algum documento css dentro da pasata assets
                persistence = True,           #Mantem o valor até que , no type memory, a página dê um refresh
                persistence_type = 'memory',
            ),
        ]
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig_bar_global
    ),

    dcc.Graph(
        id='example-graph_2',
        figure=fig_bar_global_2
    )
])



if __name__=="__main__":
    app.run_server(debug=True) 