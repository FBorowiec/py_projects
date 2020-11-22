from math import pi
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.layouts import column


class DataVisualizer:
    def __init__(self, data):
        self.data = data
        self.output_file = output_file("AAPL, AMZN, GOOG, MSFT closing rates")

    def __setup_figure__(self):
        self.f = figure(sizing_mode="stretch_both", x_axis_type="datetime")

    def plot_data(self):
        names = ("AAPL", "AMZN", "GOOG", "MSFT")

        plots = []
        for company, name in zip(self.data, names):
            inc = company["Close"] > company["Open"]
            dec = company["Open"] > company["Close"]
            w = 12 * 60 * 60 * 1000  # half day in ms

            TOOLS = "pan,wheel_zoom,box_zoom,reset,save"

            s = figure(
                sizing_mode="stretch_both",
                x_axis_type="datetime",
                tools=TOOLS,
                plot_width=1800,
                title=name + " Candlestick",
            )
            s.title.text = name
            s.title.text_font = "arial"
            s.title.text_font_style = "bold"
            s.xaxis.minor_tick_line_color = None
            s.yaxis.minor_tick_line_color = None
            s.xaxis.axis_label = "Daily data over a 3 months period"
            s.yaxis.axis_label = "Closing Value [USD]"

            s.xaxis.major_label_orientation = pi / 4.0
            s.grid.grid_line_alpha = 0.3

            s.segment(
                company["Day"],
                company["High"],
                company["Day"],
                company["Low"],
                color="black",
            )
            s.vbar(
                company["Day"][inc],
                w,
                company["Open"][inc],
                company["Close"][inc],
                fill_color="#D5E1DD",
                line_color="black",
            )
            s.vbar(
                company["Day"][dec],
                w,
                company["Open"][dec],
                company["Close"][dec],
                fill_color="#F2583E",
                line_color="black",
            )

            plots.append(s)

        p = column(plots[0], plots[1], plots[2], plots[3])

        show(p)
