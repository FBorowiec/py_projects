load("@rules_python//python:defs.bzl", "py_binary", "py_library")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_library(
    name = "coronavirus_heatmap_lib",
    srcs = [
        "request_handler.py",
        "parser.py",
        "map_generator.py"
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
