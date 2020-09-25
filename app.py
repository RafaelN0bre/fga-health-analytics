import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio

#Defindo Dataframe
df_global = pd.read_excel('covid_global.xlsx')


df_global = df_global[df_global['location']=='Afghanistan']

#Definindo Gráficos
fig_bar_global = go.Figure( data = [
    go.Bar(x = df_global['date'], y = df_global['total_cases'], name ='Casos', marker_color = "yellow"),
    go.Bar(x = df_global['date'], y = df_global['total_deaths'], name ='Mortes', marker_color = "red"),
])
fig_bar_global.update_layout(barmode='overlay')
fig_bar_global.show()

#fig_bar_global.show()

#data = [barra_global]

#layout = dict(title='Global Covid', showlegend=False)
#
#fig = dict(data=data, layout=layout)



#
#app = dash.Dash()
#
#app.layout = html.Div([
#    html.Div(html.H1(children="Hello World")),
#    html.Label("Dash Graph"),
#    html.Div(
#        dcc.Graph(id="Global Covid",
#        figure=fig)
#    )
#])
#
#if __name__=="__main__":
#    app.run_server(debug=True) 