load("@rules_python//python:defs.bzl", "py_library")
load("@3rdparty//:requirements.bzl", "requirement")


package(default_visibility = ["//visibility:public"])

py_library(
  name = "home",
  srcs = ["home.py"],
  deps = [
    requirement("flask")
  ]
)

py_library(
  name = "about",
  srcs = ["about.py"],
  deps = [
    requirement("flask")
  ]
)
