load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "data_visualization_with_bokeh",
    srcs = ["data_visualization_with_bokeh.py"],
    main = "data_visualization_with_bokeh.py",
    deps = [
        requirement("bokeh"),
        requirement("pandas"),
        requirement("xlrd"),
    ],
)

py_binary(
    name = "financial_data_visualization",
    srcs = [
        "data_parser.py",
        "data_visualizer.py",
        "financial_data_visualization.py",
        "request_handler.py",
    ],
    main = "financial_data_visualization.py",
    deps = [
        requirement("bokeh"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "financial_data_visualization_local",
    srcs = [
        "data_parser.py",
        "data_visualizer.py",
        "financial_data_visualization_local.py",
        "request_handler.py",
    ],
    data = [
        "AAPL.json",
        "AMZN.json",
        "GOOG.json",
        "MSFT.json",
    ],
    main = "financial_data_visualization_local.py",
    deps = [
        requirement("bokeh"),
        requirement("pandas"),
    ],
)
