load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_library(
    name = "coronavirus_heatmap_lib",
    srcs = [
        "map_generator.py",
        "parser.py",
        "request_handler.py",
    ],
    deps = [
        requirement("folium"),
        requirement("pandas"),
    ],
)

py_binary(
    name = "coronavirus_heatmap",
    srcs = ["coronavirus_heatmap.py"],
    main = "coronavirus_heatmap.py",
    deps = [":coronavirus_heatmap_lib"],
)
