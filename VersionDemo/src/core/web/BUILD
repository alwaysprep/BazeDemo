load("@rules_python//python:defs.bzl", "py_library")
load("@core//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])


py_library(
    name="app",
    srcs=["app.py"],
    deps=[
        requirement("flask")
    ]
)
