load("@io_bazel_rules_docker//python3:image.bzl", "py3_image")


package(default_visibility = ["//visibility:public"])


py3_image(
    name = "app",
    srcs = [
        "app.py"
    ],
    deps=[
        "//src:home"
    ]    
)
