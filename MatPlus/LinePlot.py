import matplotlib.pyplot as plt

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
        for x_data, y_data in zip(self.x, self.y):
            plt.plot(x_data, y_data, linewidth=self.linewidth)
        plt.xlim(self.lowerlimx, self.upperlimx)
        plt.ylim(self.lowerlimy, self.upperlimy)
        plt.show()
