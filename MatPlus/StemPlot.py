import matplotlib.pyplot as plt
import numpy as np


class StemPlot:
    def __init__(
        self,
        x,
        y,
        lowerlimx=None,
        lowerlimy=None,
        upperlimx=None,
        upperlimy=None,
        linefmt="-",
        markerfmt="o",
        basefmt=" ",
        label=None,  # Keep for backward compatibility but it won't be used
        orientation="vertical",
    ):
        """
        A class to create stem plots with optional axis limits and styling.
        Parameters:
        x : array-like
            The x-values of the stem plot.
        y : array-like
            The y-values of the stem plot.
        lowerlimx : float, optional
            The lower limit of the x-axis.
        lowerlimy : float, optional
            The lower limit of the y-axis.
        upperlimx : float, optional
            The upper limit of the x-axis.
        upperlimy : float, optional
            The upper limit of the y-axis.
        linefmt : str, optional
            A string defining the properties of the vertical lines in the stem plot.
        markerfmt : str, optional
            A string defining the properties of the markers at the stem heads.
        basefmt : str, optional
            A string defining the properties of the baseline.
        label : str, optional
            The label for the stem plot.
        orientation : str, optional
            The orientation of the stem plot, either 'vertical' or 'horizontal'.
        """

        self.x = np.array(x)
        self.y = np.array(y)
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy
        self.linefmt = linefmt
        self.markerfmt = markerfmt
        self.basefmt = basefmt
        self.label = label
        self.orientation = orientation

        # Set default axis limits if not provided
        # Lower limit for x-axis/y-axis
        if lowerlimx is None:
            self.lowerlimx = 0.9 * min(self.x) if self.x.size > 0 else 0
        if lowerlimy is None:
            self.lowerlimy = 0.9 * min(self.y) if self.y.size > 0 else 0
        # Upper limit for x-axis/y-axis
        if upperlimx is None:
            self.upperlimx = 1.1 * max(self.x) if self.x.size > 0 else 0
        if upperlimy is None:
            self.upperlimy = 1.1 * max(self.y) if self.y.size > 0 else 0

    def plot(self):
        """
        Constructs all the necessary attributes for the StemPlot object.
        Plot the stem plot with the given parameters.
        """
        # Plots the stem plot with the given parameters.
        fig, ax = plt.subplots()

        if self.orientation == "vertical":
            ax.stem(
                self.x,
                self.y,
                linefmt=self.linefmt,
                markerfmt=self.markerfmt,
                basefmt=self.basefmt,
                label=self.label,
            )
            ax.set_xlim(self.lowerlimx, self.upperlimx)
            ax.set_ylim(self.lowerlimy, self.upperlimy)
        elif self.orientation == "horizontal":
            ax.stem(
                self.y,
                self.x,
                linefmt=self.linefmt,
                markerfmt=self.markerfmt,
                basefmt=self.basefmt,
                label=self.label,
            )
            ax.set_ylim(self.lowerlimx, self.upperlimx)
            ax.set_xlim(self.lowerlimy, self.upperlimy)

        if self.label:
            ax.legend()
        plt.show()
