load("@rules_python//python:defs.bzl", "py_binary")


py_binary(
  name = "app",
  srcs = ["app.py"],
  deps = [
    "//src:home"
  ],
  data=[
    "//examples/apps/app_b:app_b.conf.json"
  ]
)
