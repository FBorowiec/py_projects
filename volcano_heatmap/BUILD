load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")
py_binary(
    name = "volcano_heatmap",
    srcs = ["volcano_heatmap.py"],
    main = "volcano_heatmap.py",
    deps = [
        requirement("folium"),
        ],
)
