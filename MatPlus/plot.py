import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

class plot():
    def __init__(self,x,y,lowerlimx = None,lowerlimy = None, upperlimx = None, upperlimy = None):
        """Initializes Scatterplot object with the following parameters:
        type: type of the plot
        x: x-axis data
        y: y-axis data
        lowerlimx: lower limit of x-axis
        lowerlimy: lower limit of y-axis
        upperlimx: upper limit of x-axis
        upperlimy: upper limit of y-axis
        sizes: size of the data points
        colors: color of the data points
        vmin: minimum value of the color map
        vmax: maximum value of the color map
        """
        self.x = x
        self.y = y
        self.lowerlimx = lowerlimx
        self.lowerlimy = lowerlimy
        self.upperlimx = upperlimx
        self.upperlimy = upperlimy
        if self.lowerlimx == None:
            self.lowerlimx = np.min(x) * 0.9
        if self.lowerlimy == None:
            self.lowerlimy = np.min(y) * 0.9
        if self.upperlimx == None:
            self.upperlimx = np.max(x) * 1.1
        if self.upperlimy == None:
            self.upperlimy = np.max(y) * 1.1
    




