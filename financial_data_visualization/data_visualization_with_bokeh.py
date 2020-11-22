import pandas as pd
import xlrd

from bokeh.plotting import figure
from bokeh.io import output_file, show


def plot_no_of_women_engeneering_graduates():
    df = pd.read_csv("http://pythonhow.com/data/bachelors.csv")
    x = df["Year"]
    y = df["Engineering"]

    output_file("WEngineeringGraduates.html")

    f = figure(plot_width=800, plot_height=800, tools="pan")
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


def plot_weather_data():
    df = pd.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx", sheet_name=0)
    df["Temperature"] = df["Temperature"] / 10
    df["Pressure"] = df["Pressure"] / 10

    output_file("Weather.html")

    f = figure(plot_width=800, plot_height=800, tools="pan")
    f.title.text = "Temperature and air pressure"
    f.title.text_color = "Gray"
    f.title.text_font = "arial"
    f.title.text_font_style = "bold"
    f.xaxis.minor_tick_line_color = None
    f.yaxis.minor_tick_line_color = None
    f.xaxis.axis_label = "Temperature ('C)"
    f.yaxis.axis_label = "Pressure (hPa)"

    f.circle(df["Temperature"], df["Pressure"], size=0.5)

    show(f)


if __name__ == "__main__":
    plot_no_of_women_engeneering_graduates()
    plot_weather_data()
