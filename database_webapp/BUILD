load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "database_webapp",
    srcs = [
        "email_sender.py",
        "main.py",
    ],
    data = glob([
        "static/*.css",
        "templates/*.html",
    ]),
    imports = [
        ".",
        "static/css",
        "static/templates",
    ],
    main = "main.py",
    deps = [
        requirement("flask"),
        requirement("Flask-SQLAlchemy"),
        requirement("psycopg2"),
    ],
)
