import matplotlib.pyplot as plt
import numpy as np

plt.style.use("_mpl-gallery")


class LinePlot:
    def __init__(
        self,
        x,
        y,
        lowerlimx=None,
        lowerlimy=None,
        upperlimx=None,
        upperlimy=None,
        wd=None,
        lw=None,
    ):
        self.x = x
        self.y = y
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy
        self.width = wd
        self.linewidth = lw

    def plot(self):
        plt.figure()
        for i in range(len(self.x)):
            plt.plot(self.x[i], self.y[i], linewidth=self.linewidth)
        plt.xlim(self.lowerlimx, self.upperlimx)
        plt.ylim(self.lowerlimy, self.upperlimy)
        plt.show()
