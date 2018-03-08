import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt; plt

def simplify_borders(ax):
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.tick_params(direction='out')
