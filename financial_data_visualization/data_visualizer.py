from bokeh.plotting import figure
from bokeh.io import output_file, show


class DataVisualizer:
    def __init__(self, data):
        self.data = data
        self.__setup_figure__()
        self.output_file = output_file("AAPL, AMZN, GOOG, MSFT closing rates")

    def __setup_figure__(self):
        self.f = figure(width=800, height=800, x_axis_type="datetime")
        self.f.title.text = "AAPL, AMZN, GOOG, MSFT"
        self.f.title.text_font = "arial"
        self.f.title.text_font_style = "bold"
        self.f.xaxis.minor_tick_line_color = None
        self.f.yaxis.minor_tick_line_color = None
        self.f.xaxis.axis_label = "Daily data over a 3 months period"
        self.f.yaxis.axis_label = "Closing Value [USD]"

    def plot_data(self):
        colors = ("black", "orange", "green", "blue")
        for company, color in zip(self.data, colors):
            x = company["Day"]
            y = company["Close"]
            self.f.line(x, y, line_width=2, color=color)

        show(self.f)
