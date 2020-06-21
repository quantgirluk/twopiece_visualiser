import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from apps.utils import *
from app import app

tab_shape = html.Div(
    style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '40px 20px 10px 20px ',
        'margin-left': '20px',
        'margin-right': '20px',
    },
    children=[
        dbc.Row(
            children=[
                html.Div(
                    style={
                        'padding': '25px 100px 25px 100px',
                        'color': 'black',
                        'textAlign': 'left',
                    },
                    children=[
                        dcc.Dropdown(id='distribution-tpshape',
                                     options=[
                                         {'label': 'Two-Piece Shape Student',
                                          'value': 'tpshastudent'},
                                         {'label': 'Two-Piece Shape SinhArcSinh',
                                          'value': 'tpshasas'},
                                         {
                                             'label': 'Two-Piece Shape Generalised Normal or Exponential Power',
                                             'value': 'tpshagennorm'},
                                     ],
                                     value='tpshastudent',
                                     persistence=True,
                                     persistence_type='memory',
                                     ),
                        dcc.Graph(id='tp-graph-tp-shape',
                                  figure=fig0_shape),
                    ]
                ),
                html.Div(
                    className="three columns",
                    style={
                        'color': 'black',
                        'padding': '25px 50px 25px 10px',
                        'textAlign': 'center',
                        'width': "600px",
                    },
                    children=[html.Label("Scale Parameter"),
                              dcc.Slider(
                                  id='slider-sigma-tpshape',
                                  min=0.01,
                                  max=20,
                                  step=0.5,
                                  marks={i: 'scale = {:.0f}'.format(i) for i in range(5, 20, 5)},
                                  value=1.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              html.Label("Shape Parameters"),
                              dcc.Slider(
                                  id='slider-shape1-tpshape',
                                  min=0.01,
                                  max=20,
                                  step=0.1,
                                  marks={i: 'shape1 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=5.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              dcc.Slider(
                                  id='slider-shape2-tpshape',
                                  min=0.01,
                                  max=20,
                                  step=0.1,
                                  marks={i: 'shape2 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=5.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),

                              html.Label("Sample Size"),
                              dcc.Slider(
                                  id='slider-n-tpshape',
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
            ],
        ),
        html.Div(id='tab-shape-content')
    ],
)


@app.callback(dash.dependencies.Output('tp-graph-tp-shape', 'figure'),
              [dash.dependencies.Input('distribution-tpshape', 'value'),
               dash.dependencies.Input('slider-shape1-tpshape', 'value'),
               dash.dependencies.Input('slider-shape2-tpshape', 'value'),
               dash.dependencies.Input('slider-sigma-tpshape', 'value'),
               dash.dependencies.Input('slider-n-tpshape', 'value')]
              )
def update_figure2(name, sh1, sh2, scale, n):
    sample, x, y = generate_sample_shape(name=name, n=n, scale=scale, sh1=sh1, sh2=sh2)
    bz = get_bin_size(sample)
    fig = ff.create_distplot([sample], ['sample'], bin_size=bz, show_curve=False, colors=graphs_colors['shape'])
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))

    fig.update_layout(
        width=975,
        height=700,
        margin=dict(l=50, r=50, t=20, b=20),
        paper_bgcolor="white",
    )

    return fig
