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
            html.Img(src='/assets/logo_fga.png'),
            html.P('Hello Dash'),
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