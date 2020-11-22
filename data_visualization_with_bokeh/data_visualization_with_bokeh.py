import pandas as pd

from bokeh.plotting import figure
from bokeh.io import output_file, show

df = pd.read_csv("http://pythonhow.com/data/bachelors.csv")
print(df.head())
x = df["Year"]
y = df["Engineering"]

output_file("line.html")

f = figure(plot_width=800, plot_height=800, tools="pan", logo=None)
f.title.text = "No of Women Graduates in Engineering since 1970"
f.title.text_color = "Gray"
f.title.text_font = "times"
f.title.text_font_style = "bold"
f.xaxis.minor_tick_line_color = None
f.yaxis.minor_tick_line_color = None
f.xaxis.axis_label = "Year"
f.yaxis.axis_label = "No of Graduates"

f.line(x, y)

show(f)
