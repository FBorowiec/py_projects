load("@rules_python//python:defs.bzl", "py_binary")
load("@py_projects_deps//:requirements.bzl", "requirement")

py_binary(
    name = "face_detection",
    srcs = ["face_detection.py"],
    data = [
        "haarcascade_frontalface_default.xml",
        "picture.jpg",
    ],
    main = "face_detection.py",
    deps = [
        requirement("opencv-python"),
    ],
)

py_binary(
    name = "webcam_motion_detector",
    srcs = ["webcam_motion_detector.py"],
    data = [
        "haarcascade_frontalface_default.xml",
    ],
    main = "webcam_motion_detector.py",
    deps = [
        requirement("opencv-python"),
        requirement("pandas"),
    ],
)
