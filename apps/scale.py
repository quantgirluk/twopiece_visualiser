import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from apps.utils import *
from app import app

tab_scale = html.Div(
    style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '40px 20px 10px 20px ',
        'margin-left': '20px',
        'margin-right': '20px',
    },
    children=html.Div(
        style={'padding': '25px 100px 25px 100px',
               'color': 'black',
               'textAlign': 'left',
               },
        children=[  # dbc.Row(
            #     dbc.Col([dcc.Markdown(
            #         '''The family of **two–piece scale distributions** is a family of univariate three parameter location-scale
            #         models,  where **_skewness_** is introduced by differing [scale](https://en.wikipedia.org/wiki/Scale_parameter)
            #         parameters either side of the [mode](<https://en.wikipedia.org/wiki/Mode_(statistics)>). ''',
            #         style={'padding': '10px'})]
            #     )
            # ),
            dbc.Row([
                dbc.Col([
                    # Scale
                    html.Div(
                        children=[
                            dcc.Dropdown(id='dd-distribution',
                                         options=[
                                             {'label': 'Two-Piece Normal', 'value': 'tpnorm'},
                                             {'label': 'Two-Piece Logistic', 'value': 'tplogistic'},
                                             {'label': 'Two-Piece Laplace', 'value': 'tplaplace'},
                                             {'label': 'Two-Piece Cauchy', 'value': 'tpcauchy'},
                                         ],
                                         value='tpnorm',
                                         persistence=True,
                                         persistence_type='memory',
                                         ),
                            dcc.Graph(id='tp-graph',
                                      figure=fig0,
                                      className="div-card",
                                      ),

                            html.Div(
                                style={
                                    'color': 'black',
                                    'padding': '25px 50px 25px 10px',
                                    'textAlign': 'left',
                                    'width': "700px",
                                },
                                children=[

                                    html.Label("Scale Parameters"),
                                    dcc.Slider(
                                        id='slider-sigma1',
                                        min=0.01,
                                        max=21,
                                        step=0.1,
                                        marks={i: 's1 = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                        value=1.0,
                                        tooltip={'placement': 'bottom'},
                                        persistence=True,
                                        persistence_type='memory',

                                    ),
                                    dcc.Slider(
                                        id='slider-sigma2',
                                        min=0.01,
                                        max=21,
                                        step=0.1,
                                        marks={i: 's2 = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                        value=1.0,
                                        tooltip={'placement': 'bottom'},
                                        persistence=True,
                                        persistence_type='memory',
                                    ),

                                    html.Label("Sample Size"),
                                    dcc.Slider(id='slider-n',
                                               min=100,
                                               max=2000,
                                               step=10,
                                               marks={i: 'n = {}'.format(i) for i in
                                                      range(500, 2000, 500)},
                                               value=1000,
                                               tooltip={'placement': 'bottom'},
                                               persistence=True,
                                               persistence_type='memory',
                                               ),
                                ])
                        ],
                    )], width=6),
                dbc.Col([
                    # Shape
                    html.Div(
                        children=[
                            dcc.Dropdown(id='dd-distribution-shape',
                                         options=[
                                             {'label': 'Two-Piece Student', 'value': 'tpstudent'},
                                             {'label': 'Two-Piece SinhArcSinh', 'value': 'tpsas'},
                                             {
                                                 'label': 'Two-Piece Generalised Normal or Exponential Power',
                                                 'value': 'tpgennorm'},
                                         ],
                                         value='tpstudent',
                                         persistence=True,
                                         persistence_type='memory',
                                         ),

                            dcc.Graph(id='tp-graph-shape',
                                      figure=fig1),

                            html.Div(
                                style={
                                    'color': 'black',
                                    'padding': '25px 50px 25px 10px',
                                    'textAlign': 'left',
                                    'width': "700px",
                                },
                                children=[
                                    html.Label("Scale Parameters"),
                                    dcc.Slider(
                                        id='slider-sigma1-shape',
                                        min=0.01,
                                        max=20,
                                        step=0.1,
                                        marks={i: 's1 = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                        value=1.0,
                                        persistence=True,
                                        persistence_type='memory',
                                        tooltip={'placement': 'bottom'}),
                                    dcc.Slider(
                                        id='slider-sigma2-shape',
                                        min=0.01,
                                        max=20,
                                        step=0.1,
                                        marks={i: 's2 = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                        value=1.0,
                                        tooltip={'placement': 'bottom'}),
                                    html.Label("Shape Parameter"),
                                    dcc.Slider(
                                        id='slider-shape',
                                        min=0.01,
                                        max=20,
                                        step=0.5,
                                        marks={i: 'shape = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                        value=5.0,
                                        persistence=True,
                                        persistence_type='memory',
                                        tooltip={'placement': 'bottom'}),
                                    html.Label("Sample Size"),
                                    dcc.Slider(
                                        id='slider-n-shape',
                                        min=100,
                                        max=2000,
                                        step=10,
                                        marks={i: 'n = {}'.format(i) for i in range(500, 2000, 500)},
                                        value=1000,
                                        persistence=True,
                                        persistence_type='memory',
                                        tooltip={'placement': 'bottom'}),
                                ]
                            ),
                        ]
                    )],
                    width=6)
            ])
        ],
    )
)


@app.callback(Output('tp-graph', 'figure'),
              [Input('dd-distribution', 'value'),
               Input('slider-sigma1', 'value'),
               Input('slider-sigma2', 'value'),
               Input('slider-n', 'value')]
              )
def update_figure(name, s1, s2, n):
    sample, x, y = generate_sample_scale(name=name, s1=s1, s2=s2, n=n)
    bz = get_bin_size(sample)

    fig = ff.create_distplot([sample], ['sample'], bin_size=bz,
                             show_curve=False,
                             colors=graphs_colors['scale']
                             )

    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))
    fig.update_layout(
        width=750,
        height=600,
        margin=dict(l=50, r=50, t=20, b=20),
        paper_bgcolor="white",
    )

    return fig


@app.callback(dash.dependencies.Output('tp-graph-shape', 'figure'),
              [dash.dependencies.Input('dd-distribution-shape', 'value'),
               dash.dependencies.Input('slider-sigma1-shape', 'value'),
               dash.dependencies.Input('slider-sigma2-shape', 'value'),
               dash.dependencies.Input('slider-shape', 'value'),
               dash.dependencies.Input('slider-n-shape', 'value')]
              )
def update_figure1(name, s1, s2, shape, n):
    sample, x, y = generate_sample_scale(name=name, s1=s1, s2=s2, shape=shape, n=n)
    bz = get_bin_size(sample)

    fig = ff.create_distplot([sample], ['sample'], bin_size=bz,
                             show_curve=False, colors=graphs_colors['scale_shape'])

    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))

    fig.update_layout(
        width=750,
        height=600,
        margin=dict(l=50, r=50, t=20, b=20),
        paper_bgcolor="white",
    )

    fig.layout.template = 'plotly_white'

    return fig
