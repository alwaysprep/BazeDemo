
py_test(
    name = "test_clean_data_input",
    srcs=["test_clean_data_input.py"],
    deps=[
        "//src/preprocessing:clean_data"
    ],
    data=[
        "//data:ThePhilosophersStone.txt"
    ]
)

py_test(
    name = "test_clean_data_input_output",
    srcs=["test_clean_data_input_output.py"],
    deps=[
        "//src/preprocessing:clean_data"
    ],
    data=[
        "//data:ThePhilosophersStone.txt",
        "//data:ThePhilosophersStoneStopWordsRemoved.txt"
    ]
)
