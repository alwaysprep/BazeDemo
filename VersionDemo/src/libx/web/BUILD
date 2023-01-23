load("@rules_python//python:defs.bzl", "py_library")
load("@libx//:requirements.bzl", "requirement")

package(default_visibility = ["//visibility:public"])


py_library(
    name="home",
    srcs=["home.py"],
    deps=[
        requirement("numpy"),
        "//src/core"
    ]
)
