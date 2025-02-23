import pytest
import numpy as np
from MatPlus.BoxPlot import BoxPlot
import matplotlib.pyplot as plt


def test_boxplot_creation():
    data = [1, 2, 3, 4, 5]
    boxplot = BoxPlot(data, sym="r")
    assert boxplot.data == data
    assert boxplot.sym == "r"
    assert boxplot.notch is False
    assert boxplot.vert is True
    assert boxplot.whis == 1.5


def test_boxplot_statistics():
    data = [1, 2, 3, 4, 5]
    boxplot = BoxPlot(data)

    # Test quartiles
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    median = np.median(data)

    assert np.median(boxplot.data) == median
    assert np.percentile(boxplot.data, 25) == q1
    assert np.percentile(boxplot.data, 75) == q3


def test_boxplot_parameters():
    data = [1, 2, 3, 4, 5]
    boxplot = BoxPlot(data, notch=True, sym="x", vert=False, whis=2.0)
    assert boxplot.notch is True
    assert boxplot.sym == "x"
    assert boxplot.vert is False
    assert boxplot.whis == 2.0


def test_boxplot_empty_data():
    with pytest.raises(ValueError):
        BoxPlot([])


def test_boxplot_plot():
    data = [1, 2, 3, 4, 5]
    boxplot = BoxPlot(data)
    # Just verify the plot method runs without error
    boxplot.plot()
    plt.close()  # Clean up plot
