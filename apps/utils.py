from math import log2

import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
import plotly.io as pio
from scipy.stats import norm
from twopiece.double import dtpgennorm, dtpstudent, dtpsas
from twopiece.scale import tplogistic, tplaplace, tpstudent, tpsas, tpgennorm, tpcauchy
from twopiece.scale import tpnorm
from twopiece.shape import tpshastudent, tpshagennorm, tpshasas

pio.templates.default = "plotly_white"

np.random.seed(123)


def get_bin_size(sample):
    n = len(sample)
    k = int(log2(n)) + 5
    bz = (np.max(sample) - np.min(sample)) / k

    return bz


TPSCALE = {
    'tpnorm': {'obj': tpnorm, 'shape': False, 'label': 'Two-Piece Normal'},
    'tplaplace': {'obj': tplaplace, 'shape': False, 'label': 'Two-Piece Laplace'},
    'tpcauchy': {'obj': tpcauchy, 'shape': False, 'label': 'Two-Piece Cauchy'},
    'tplogistic': {'obj': tplogistic, 'shape': False, 'label': 'Two-Piece Logistic'},
    'tpstudent': {'obj': tpstudent, 'shape': True, 'label': 'Two-Piece Student'},
    'tpsas': {'obj': tpsas, 'shape': True, 'label': 'Two-Piece SAS'},
    'tpgennorm': {'obj': tpgennorm, 'shape': True, 'label': 'Two-Piece Gen. Normal'},
}

TPSHAPE = {
    'tpshastudent': {'obj': tpshastudent, 'shape': True, 'label': 'Two-Piece Shape Student'},
    'tpshasas': {'obj': tpshasas, 'shape': True, 'label': 'Two-Piece SAS'},
    'tpshagennorm': {'obj': tpshagennorm, 'shape': True, 'label': 'Two-Piece Shape Gen. Normal'},
}

DTP = {
    'dtpstudent': {'obj': dtpstudent, 'shape': True, 'label': 'Two-Piece Shape Student'},
    'dtpsas': {'obj': dtpsas, 'shape': True, 'label': 'Two-Piece SAS'},
    'dtpgennorm': {'obj': dtpgennorm, 'shape': True, 'label': 'Two-Piece Shape Gen. Normal'},
}

graphs_colors = {'scale': ['#C76478'],
                 'scale_shape': ['#92DCE5'],
                 'shape': ['#119DA4'],
                 'double': ['#FFC857'],
                 'pdf': '#CD207E'}


def generate_sample_double(name, n, s1, s2, sh1, sh2):
    dist = DTP[name]['obj']
    z = dist(loc=0, sigma1=s1, sigma2=s2, shape1=sh1, shape2=sh2)
    sample = z.random_sample(size=n).tolist()
    a = np.min(sample)
    b = np.max(sample)
    x = np.linspace(a, b, 1000)
    y = z.pdf(x)

    return sample, x, y


sample0, x0, y0 = generate_sample_double(name='dtpstudent', s1=1.0, s2=1.0, sh1=5.0, sh2=5.0, n=1000)
fig0_double = ff.create_distplot([sample0], ['sample'], show_curve=False, colors=graphs_colors['double'])
fig0_double.add_trace(
    go.Scatter(x=x0, y=y0, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))
fig0_double.update_layout(
    width=975,
    height=700,
    margin=dict(l=50, r=50, t=20, b=20),
    paper_bgcolor="white",
)


def generate_sample_shape(name, n, scale, sh1, sh2):
    dist = TPSHAPE[name]['obj']
    z = dist(loc=0, sigma=scale, shape1=sh1, shape2=sh2)
    sample = z.random_sample(size=n).tolist()
    a = np.min(sample)
    b = np.max(sample)
    x = np.linspace(a, b, 1000)
    y = z.pdf(x)

    return sample, x, y


sample0, x0, y0 = generate_sample_shape(name='tpshastudent', scale=1.0, sh1=5.0, sh2=5.0, n=1000)
fig0_shape = ff.create_distplot([sample0], ['sample'], show_curve=False, colors=graphs_colors['shape'])
fig0_shape.add_trace(go.Scatter(x=x0, y=y0, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))
fig0_shape.update_layout(
    width=975,
    height=700,
    margin=dict(l=50, r=50, t=20, b=20),
    paper_bgcolor="white",
)


def generate_sample_scale(name, n, s1, s2, shape=None):
    dist = TPSCALE[name]['obj']
    if TPSCALE[name]['shape']:
        z = dist(sigma1=s1, sigma2=s2, shape=shape)
    else:
        z = dist(sigma1=s1, sigma2=s2)

    sample = z.random_sample(size=n).tolist()

    a = np.min(sample)
    b = np.max(sample)
    x = np.linspace(a, b, 1000)
    y = z.pdf(x)

    return sample, x, y


sample0, x0, y0 = generate_sample_scale(name='tpnorm', s1=1.0, s2=1.0, n=1000)
bz0 = get_bin_size(sample0)
fig0 = ff.create_distplot([sample0], ['sample'], show_curve=False, colors=graphs_colors['scale'])
fig0.add_trace(go.Scatter(x=x0, y=y0, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))
fig0.update_layout(
    width=750,
    height=600,
    margin=dict(l=50, r=50, t=20, b=20),
    paper_bgcolor="white",
)

sample1, x1, y1 = generate_sample_scale(name='tpstudent', s1=1.0, s2=1.0, shape=5.0, n=1000)
bz1 = get_bin_size(sample1)
fig1 = ff.create_distplot([sample1], ['sample'], show_curve=False, colors=graphs_colors['scale_shape'])
fig1.add_trace(go.Scatter(x=x1, y=y1, mode='lines', name='pdf', line=dict(color=graphs_colors['pdf'], width=2.0)))
fig1.update_layout(
    width=750,
    height=600,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="white",
)

mu = 0
sigma1 = 1
sigma2 = 1.75

tpn = tpnorm(mu, sigma1, sigma2)

fig_tpnormal = go.Figure()
fig_tpnormal.add_trace(go.Scatter(x=np.arange(-6, 6.5, 0.1), y=tpn.pdf(np.arange(-6, 6.5, 0.1)), mode='lines',
                                  name='Two-Piece Normal',
                                  line=dict(color='pink', width=1.0), fill='tonexty'))
fig_tpnormal.add_trace(go.Scatter(x=np.arange(-6, 0.0, 0.1),
                                  y=norm.pdf(np.arange(-6, 0.0, 0.1), mu, sigma1), mode='lines',
                                  name='Left Normal pdf',
                                  line=dict(color='blue', width=1.0)))
fig_tpnormal.add_trace(go.Scatter(x=np.arange(0, 6.5, 0.1),
                                  y=norm.pdf(np.arange(0, 6.5, 0.1), mu, sigma2), mode='lines',
                                  name='Right Normal pdf',
                                  line=dict(color='purple', width=1.0)))
fig_tpnormal.update_layout(
    width=700,
    height=300,
    margin=dict(l=50, r=50, t=20, b=20),
    paper_bgcolor="white",
)
