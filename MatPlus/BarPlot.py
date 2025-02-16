import matplotlib.pyplot as plt
import numpy as np

class BarPlot():

    def __init__(self,x,y,lowerlimx = None,lowerlimy = None, upperlimx = None, upperlimy = None, wd = None, lw = None):
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
        
        self.width = wd
        self.linewidth = lw

        if self.linewidth == None:
            self.linewidth = 1
        if self.width == None:
            self.width = 1
    

    def plot(self):
        
        plt.style.use('_mpl-gallery')
        fig, ax = plt.subplots()
        ax.bar(x, y, width=self.width, edgecolor="black", linewidth=1)
        ax.set(xlim=(self.lowerlimx, self.upperlimx), xticks=np.arange(self.lowerlimx+1, self.upperlimx),
            ylim=(self.lowerlimy, self.upperlimy), yticks=np.arange(self.lowerlimy+1, self.upperlimy))
        plt.show()



