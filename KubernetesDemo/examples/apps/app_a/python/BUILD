load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
  name = "app",
  srcs = ["app.py"],
  deps = [
    "//src:home",
    "//src:about"
  ],
  data=[
    "//examples/apps/app_a:app_a.conf.json"
  ]
)
