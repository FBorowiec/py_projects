load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "bookshop_database",
    srcs = [
        "backend_database.py",
        "bookshop_database.py",
        "frontend_gui.py",
    ],
    main = "bookshop_database.py",
    deps = [
        requirement("psycopg2"),
    ],
)
