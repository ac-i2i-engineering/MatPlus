import numpy as np
from MatPlus.StemPlot import StemPlot


def test_stemplot_initialization():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = StemPlot(x, y)
    assert plot.lowerlimx == 0.9 * np.min(x)
    assert plot.upperlimx == 1.1 * np.max(x)
    assert plot.lowerlimy == 0.9 * np.min(y)
    assert plot.upperlimy == 1.1 * np.max(y)
    assert plot.linefmt == "-"
    assert plot.markerfmt == "o"
    assert plot.basefmt == " "
    assert plot.orientation == "vertical"


def test_stemplot_with_limits():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = StemPlot(x, y, lowerlimx=0, upperlimx=4, lowerlimy=0, upperlimy=4)
    assert plot.lowerlimx == 0
    assert plot.upperlimx == 4
    assert plot.lowerlimy == 0
    assert plot.upperlimy == 4


def test_stemplot_with_orientation():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = StemPlot(x, y, orientation="horizontal")
    assert plot.orientation == "horizontal"


def test_stemplot_with_custom_styles():
    x = [1, 2, 3]
    y = [1, 2, 3]
    plot = StemPlot(x, y, linefmt="--", markerfmt="s", basefmt="r")
    assert plot.linefmt == "--"
    assert plot.markerfmt == "s"
    assert plot.basefmt == "r"


def test_stemplot_empty_data():
    x = []
    y = []
    plot = StemPlot(x, y)
    assert plot.lowerlimx == 0
    assert plot.upperlimx == 0
    assert plot.lowerlimy == 0
    assert plot.upperlimy == 0
