load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "mp3_metadata_editor",
    srcs = ["mp3_metadata_editor.py"],
    deps = [
        requirement("mutagen"),
    ],
)
