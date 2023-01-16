
py_test(
    name = "test_stop_words_input",
    srcs=["test_stop_words_input.py"],
    deps=[
        "//src/preprocessing:stop_words"
    ],
    data=[
        "//data:ThePhilosophersStone.txt"
    ]
)

py_test(
    name = "test_stop_words_input_output",
    srcs=["test_stop_words_input_output.py"],
    deps=[
        "//src/preprocessing:stop_words"
    ],
    data=[
        "//data:ThePhilosophersStone.txt",
        "//data:ThePhilosophersStoneStopWordsRemoved.txt"
    ]
)


py_test(
    name = "test_punctuation_input",
    srcs=["test_punctuation_input.py"],
    deps=[
        "//src/preprocessing:punctuation"
    ],
    data=[
        "//data:ThePhilosophersStone.txt"
    ]
)


py_test(
    name = "test_punctuation_input_output",
    srcs=["test_punctuation_input_output.py"],
    deps=[
        "//src/preprocessing:punctuation"
    ],
    data=[
        "//data:ThePhilosophersStone.txt",
        "//data:ThePhilosophersStonePunctuationsRemoved.txt"
    ]
)

py_test(
    name = "test_punctuation_stop_words_input_output",
    srcs=["test_punctuation_stop_words_input_output.py"],
    deps=[
        "//src/preprocessing:punctuation",
        "//src/preprocessing:stop_words"
    ],
    data=[
        "//data:ThePhilosophersStone.txt",
        "//data:ThePhilosophersStonePunctuationsStopWordsRemoved.txt"
    ]
)
