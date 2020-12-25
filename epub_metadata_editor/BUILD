load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "epub_metadata_editor",
    srcs = ["epub_metadata_editor.py"],
    deps = [
        requirement("EbookLib"),
    ],
)
