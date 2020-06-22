import dash_core_components as dcc
import dash_html_components as html
from apps.utils import fig_tpnormal

tab_welcome = html.Div(
    style={
        'borderLeft': '1px solid #d6d6d6',
        'borderRight': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'padding': '44px',
        'margin-left': '20px',
        'margin-right': '20px',

    },
    children=[
        html.Div(
            style={'padding': '25px 100px 25px 100px',
                   'color': 'black',
                   'textAlign': 'left',
                   'width': '100%'
                   },
            children=[html.H5('What is a Two-Piece Distribution?'),

                      dcc.Markdown(
                          '''
                          In simple words, the **two-piece distributions** result from joining (at the 
                          [mode](<https://en.wikipedia.org/wiki/Mode_(statistics)>)) 
                          the corresponding halves of a continuous, symmetric distribution using the same location 
                          parameter  but possibly different [scale](https://en.wikipedia.org/wiki/Scale_parameter) 
                          and [shape](https://en.wikipedia.org/wiki/Shape_parameter) 
                          parameters to introduce **_skewness_**. Probably the most famous member of this family is the 
                          [Two-Piece Normal](https://quantgirl.blog/two-piece-normal/) which is also known as 
                          [split normal](https://en.wikipedia.org/wiki/Split_normal_distribution), binormal, 
                          or double-Gaussian. This distribution results from joining at the mode the corresponding
                          halves of two normal distributions with the same mode  but different standard deviations.
                          This idea can be seen in the following graph where we can see the two half 
                          densities in blue and purple and the resulting two-piece normal density in pink.
                          ''',
                          style={
                              "margin-left": "auto",
                              "margin-right": "auto",
                              'padding': '10px 0px 0px 10px'

                          }

                      ),

                      # html.Ul(
                      #     children=[
                      #         html.Li('test1'),
                      #         html.Li('test2'),
                      #     ],
                      #     style={'padding': '10px'}
                      # ),

                      dcc.Graph(id='tpnormal',
                                figure=fig_tpnormal,
                                style={
                                    'margin': 'auto', 'width': "50%",
                                    "display": "block"}
                                ),

                      html.H5(className='what-is',
                              children='What is Two-Piece Distributions Visualiser?'),
                      dcc.Markdown('It is a [Dash](https://dash.plotly.com/) app that provides visualisations of '
                                   'the density functions for the most '
                                   'popular two-piece distributions. '
                                   'It allows you to change scale and shape parameters and see the effect '
                                   'on the density functions showing the high flexibility of this family of '
                                   'distributions. '
                                   'It covers the three subfamilies of Two-Piece distributions:',
                                   style={'padding': '10px 0px 0px 10px'}
                                   ),

                      dcc.Markdown(
                          '''
                          * Scale: where skewness is introduced by differing only the scale parameters 
                          either side of the mode. 
                          * Shape: where skewness is introduced by differing only the shape parameters
                          either side of the mode.
                          * Double: where skewness is introduced by differing both scale and shape parameters 
                          either side of the mode.
                          
                          Feel free to explore each family in their corresponding tab.
                      
                          ''',
                          style={'padding': '0px 0px 0px 20px'}
                      ),

                      html.H5("References"),

                      dcc.Markdown(
                          '''For the [Python](https://www.python.org/) implementation of the twopiece family please
                          visit my Git repoitory [twopiece](https://github.com/quantgirluk/twopiece). 
                          You can find details on the latest release in my blog entry
                          [twopiece-1.2.0](https://quantgirl.blog/twopiece-1-2-0/)             
                          ''',
                          style={'padding': '10px 0px 0px 10px'}
                      ),

                      dcc.Markdown(
                          '''For the [R](https://www.r-project.org/) implementation of the twopiece family we refer to
                           the following packages: 
                           [twopiece, DTP, and TPSAS](https://sites.google.com/site/fjavierrubio67/resources)            
                          ''',
                          style={'padding': '0px 0px 0px 10px'}
                      ),

                      dcc.Markdown(
                          '''For technical details on these families of distributions we refer to 
                          the following two publications which serve as reference for the twopiece Python implementation.
                          ''',
                          style={'padding': '0px 0px 0px 10px'}
                      ),
                      dcc.Markdown(
                          '''
                          * [Inference in Two-Piece Location-Scale Models with 
                          Jeffreys Priors](https://projecteuclid.org/euclid.ba/1393251764) 
                          published in [Bayesian Anal.](https://projecteuclid.org/euclid.ba) Volume 9, 
                          Number 1 (2014), 1-22.
                          * [Bayesian modelling of skewness and kurtosis with 
                          Two-Piece Scale and shape distributions](https://projecteuclid.org/euclid.ejs/1440680330) 
                          published in [Electron. J. Statist.](https://projecteuclid.org/euclid.ejs), 
                          Volume 9, Number 2 (2015), 1884-1912.
                          ''',
                          style={'padding': '0px 0px 0px 20px'}
                      ),

                      ])
    ],
)
