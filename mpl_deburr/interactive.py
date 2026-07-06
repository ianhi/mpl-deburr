from contextlib import contextmanager

from matplotlib import pyplot as plt

__all__ = [
    "print_figsize",
    "print_set_xy_lims",
    "current_axes",
]


def print_figsize(fig=None):
    """
    print out a figure's figsize ready to be copy pasted into a plt.figure command.
    Useful after manually adjusting figuring size.

    Parameters
    ----------
    fig : matplotlib.figure.Figure or None
        The figure to use, if *None* then use the current figure
    """
    if fig is None:
        fig = plt.gcf()
    print(f"figsize = ({fig.get_figwidth:0.2f}, {fig.get_figheight:0.2f}")


def print_set_xy_lims(ax=None, ax_name: str = "ax"):
    """
    Print out an axes' x and ylims to be set
    useful when interactively sizing something and wanting to make it permanent.

    Parameters
    ----------
    ax : matplotlib.axis.Axes or None
        The axis to use, if *None* then use the current axis
    ax_name : str, default 'ax'
        The name to use when printing out code.
    """
    if ax is None:
        ax = plt.gca()

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    print(f"{ax_name}.set_xlim({xlim[0]:0.3f}, {xlim[1]:0.3f})")
    print(f"{ax_name}.set_ylim({ylim[0]:0.3f}, {ylim[1]:0.3f})")


@contextmanager
def current_axes(ax):
    """
    Set the current
    Parameters
    ----------
    ax : matplotlib.axis.Axes
    """
    prev_ax = plt.gca()
    plt.sca(ax)
    yield
    plt.sca(prev_ax)
