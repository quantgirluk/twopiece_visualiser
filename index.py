import dash_core_components as dcc
import dash_html_components as html
import plotly.io as pio
from dash.dependencies import Input, Output

from app import app, server
from apps import welcome, scale, shape, double

colors = {
    'background': "#732364",
    'text': 'white'
}

pio.templates.default = "plotly_white"

app.layout = html.Div(
    children=[

        html.Div(
            style={'padding': '25px 50px 25px 100px',
                   'backgroundColor': colors['background'],
                   'color': colors['text'],
                   'textAlign': 'center',
                   },
            children=[
                html.H2('Two-Piece Distributions Visualiser',
                        style={'textAlign': 'center',
                               'margin-top': '48px',
                               'fontFamily': 'sans-serif'}),
                # html.H6("Visualise the family of two-piece distributions!"),

            ],
        ),
        dcc.Tabs(id="tabs",
                 style={
                     'borderLeft': '1px solid #d6d6d6',
                     'borderRight': '1px solid #d6d6d6',
                     'margin-left': '20px',
                     'margin-right': '20px',

                 },
                 value='tab-welcome-value',
                 children=[
                     dcc.Tab(id='tab-welcome',
                             label='Welcome',
                             value='tab-welcome-value'
                             ),
                     dcc.Tab(id='tab-scale',
                             label='Two Piece Scale',
                             value='tab-scale-value',
                             ),
                     dcc.Tab(id='tab-shape',
                             label='Two-Piece Shape',
                             value='tab-shape-value',

                             ),
                     dcc.Tab(id='tab-double',
                             label='Double Two-Piece',
                             value='tab-double-value',
                             )
                 ],
                 ),
        html.Div(id='tabs-content',
                 children=welcome.tab_welcome
                 )
    ])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-welcome-value':
        return welcome.tab_welcome
    elif tab == 'tab-scale-value':
        return scale.tab_scale
    elif tab == 'tab-shape-value':
        return shape.tab_shape
    elif tab == 'tab-double-value':
        return double.tab_double


if __name__ == '__main__':
    app.run_server(debug=True)
