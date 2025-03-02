from matplotlib import pyplot as plt
import numpy as np


class Histogram:
    """
    A class for creating line plots using matplotlib.

    The LinePlot class provides a simplified interface for creating line plots
    with customizable axis limits and line properties. It supports plotting
    multiple lines on the same figure.

    Parameters
    ----------
    x : list or list of lists
        The x-coordinates of the line(s). For multiple lines, provide a list of lists.
    y : list or list of lists
        The y-coordinates of the line(s). For multiple lines, provide a list of lists.
    lowerlimx : float, optional
        Lower limit of the x-axis. Default is None (auto-determined).
    lowerlimy : float, optional
        Lower limit of the y-axis. Default is None (auto-determined).
    upperlimx : float, optional
        Upper limit of the x-axis. Default is None (auto-determined).
    upperlimy : float, optional
        Upper limit of the y-axis. Default is None (auto-determined).
    wd : float, optional
        Width of the figure. Default is None (uses matplotlib default).
    lw : float, optional
        Line width for the plot. Default is None (uses matplotlib default).

    Examples
    --------
    >>> # Single line plot
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [1, 4, 9, 16, 25]
    >>> line_plot = LinePlot(x, y)
    >>> line_plot.plot()

    >>> # Multiple line plot
    >>> x = [[1, 2, 3], [1, 2, 3, 4]]
    >>> y = [[1, 2, 3], [4, 3, 2, 1]]
    >>> line_plot = LinePlot(x, y, lowerlimx=0, upperlimx=5)
    >>> line_plot.plot()
    """

    def __init__(self, data, bins=10, density=False, color=None):
        self.data = data
        self.bins = bins
        self.density = density
        self.color = color

    def plot(self):
        """
        Create and display a line plot.

        This method creates a matplotlib figure and plots the data
        provided during initialization. If multiple lines were provided,
        all lines will be displayed on the same plot.

        Returns
        -------
        None
            The plot is displayed but not returned.
        """
        plt.hist(self.data, bins=self.bins, density=self.density, color=self.color)
        plt.show()
