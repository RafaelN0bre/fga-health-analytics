import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from apps import dashboard_global, dashboard_local, referencias


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
    html.Div([
        dcc.Link('Global |', href='/apps/dashboard_global'),
        dcc.Link('Local |', href='/apps/dashboard_local'),
        dcc.Link('Referencias |', href='/apps/referencias'),
    ]),
    dcc.Location(id='url', refresh=False, pathname='/apps/dashboard_global'),
    html.Div(id='page-content', children=[]),
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
)
def dispaly_page(pathname):
    if pathname == '/apps/dashboard_global':
        return dashboard_global.layout
    
    elif pathname == '/apps/dashboard_local':
        return dashboard_local.layout

    elif pathname == '/apps/referencias':
        return referencias.layout

    else:
        return "404 Page Error! Please choose a link"

if __name__ == '__main__':
    app.run_server(debug=True)