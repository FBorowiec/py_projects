load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "english_dictionary",
    srcs = ["english_dictionary.py"],
    main = "english_dictionary.py",
    deps = [
        requirement("mysql-connector"),
    ],
)
