from api.nlpFilter import filterText


def test_filterText():

    with open(
        "test/unit_test/apiFunctions/nlpFilter/nlpFilter_test_case/example_input.txt",
        "r",
        encoding="utf-8",
    ) as archive:

        text_input = archive.read()

    response_test = filterText(text_input)

    with open(
        "test/unit_test/apiFunctions/nlpFilter/nlpFilter_test_case/example_output.txt",
        "r",
        encoding="utf-8",
    ) as archive:

        text_output = archive.read()

    assert text_output == response_test
