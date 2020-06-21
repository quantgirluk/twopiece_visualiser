import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from apps.utils import *
from app import app

tab_double = html.Div(
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
                        dcc.Dropdown(id='distribution-dtp',
                                     options=[
                                         {'label': 'Double Two-Piece Student',
                                          'value': 'dtpstudent'},
                                         {'label': 'Double Two-Piece SinhArcSinh',
                                          'value': 'dtpsas'},
                                         {
                                             'label': 'Double Two-Piece Generalised Normal or Exponential Power',
                                             'value': 'dtpgennorm'}, ],
                                     value='dtpstudent',
                                     persistence=True,
                                     persistence_type='memory',
                                     ),
                        dcc.Graph(id='graph-dtp',
                                  figure=fig0_double)
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
                    children=[html.Label("Scale Parameters"),
                              dcc.Slider(
                                  id='slider-sigma1-dtp',
                                  min=0.01,
                                  max=20,
                                  step=0.1,
                                  marks={i: 's1 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=1.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              dcc.Slider(
                                  id='slider-sigma2-dtp',
                                  min=0.01,
                                  max=20,
                                  step=0.1,
                                  marks={i: 's2 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=1.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              html.Label("Shape Parameters"),
                              dcc.Slider(
                                  id='slider-shape1-dtp',
                                  min=0.01,
                                  max=20,
                                  step=0.5,
                                  marks={i: 'shape1 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=5.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              dcc.Slider(
                                  id='slider-shape2-dtp',
                                  min=0.01,
                                  max=20,
                                  step=0.5,
                                  marks={i: 'shape2 = {:.0f}'.format(i) for i in
                                         range(5, 20, 5)},
                                  value=5.0,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),

                              html.Label("Sample Size"),
                              dcc.Slider(
                                  id='slider-n-dtp',
                                  min=100,
                                  max=2000,
                                  step=10,
                                  marks={i: 'n = {}'.format(i) for i in
                                         range(500, 2000, 500)},
                                  value=1000,
                                  persistence=True,
                                  persistence_type='memory',
                                  tooltip={'placement': 'bottom'}),
                              ]
                ),
            ]
        ),
        html.Div(id='tab-double-content')
    ],
)


@app.callback(dash.dependencies.Output('graph-dtp', 'figure'),
              [dash.dependencies.Input('distribution-dtp', 'value'),
               dash.dependencies.Input('slider-sigma1-dtp', 'value'),
               dash.dependencies.Input('slider-sigma2-dtp', 'value'),
               dash.dependencies.Input('slider-shape1-dtp', 'value'),
               dash.dependencies.Input('slider-shape2-dtp', 'value'),
               dash.dependencies.Input('slider-n-dtp', 'value')]
              )
def update_figure2(name, s1, s2, sh1, sh2, n):
    sample, x, y = generate_sample_double(name=name, n=n, s1=s1, s2=s2, sh1=sh1, sh2=sh2)
    bz = get_bin_size(sample)
    fig = ff.create_distplot([sample], ['sample'], bin_size=bz, show_curve=False, colors=graphs_colors['double'])
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))

    fig.update_layout(
        width=975,
        height=700,
        margin=dict(l=50, r=50, t=20, b=20),
        paper_bgcolor="white",
    )

    return fig
