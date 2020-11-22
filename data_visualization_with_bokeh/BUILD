load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "data_visualization_with_bokeh",
    srcs = ["data_visualization_with_bokeh.py"],
    data = ["input_data.csv"],
    main = "data_visualization_with_bokeh.py",
    deps = [
        requirement("bokeh"),
        requirement("pandas"),
        requirement("xlrd"),
    ],
)
