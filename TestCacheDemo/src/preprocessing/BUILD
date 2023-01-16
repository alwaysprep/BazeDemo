
package(default_visibility = ["//visibility:public"])


py_library(
    name="stop_words",
    srcs=[
        "stop_words.py"
    ],
    deps=[
        "//src/preprocessing/filter:filter_words"
    ]
)


py_library(
    name="punctuation",
    srcs=["punctuation.py"],
    deps=[
        "//src/preprocessing/filter:filter"
    ]
)


py_library(
    name="preprocessing",
    srcs=[
        "//src/preprocessing:stop_words",
        "//src/preprocessing:punctuation"
    ],
)
