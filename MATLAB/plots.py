import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def fig3d(*args, **kwargs):
    fig = plt.figure(*args, **kwargs)
    ax = fig.gca(projection='3d')
    return fig, ax


def surf(*args, **kwargs):
    _, ax = fig3d()
    return ax.plot_surface(*args, **kwargs)


def grid(*args, **kwargs):
    _, ax = fig3d()
    return ax.plot_wireframe(*args, **kwargs)
