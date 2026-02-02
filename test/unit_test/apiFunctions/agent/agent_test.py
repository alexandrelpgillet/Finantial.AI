import re
from api.agent import getInvoice


def test_getInvoice():

    with open("test/unit_test/apiFunctions/agent/agent_test_case/example.txt", "r", encoding="utf-8") as archive:
        content = archive.read()

    response = getInvoice(content)

    pattern_date = r"^\d{2}/\d{2}(/\d{2,4})?$"

    pattern_value = r"R\$ \d+,\d{2}"

    assert re.match(
        pattern_value, response.total
    ), f"Invalid total value = {response.total}"

    assert re.match(pattern_value, response.tax), f"Invalid tax value = {response.tax}"

    assert isinstance(response.spents, list)

    assert len(response.spents) > 0

    for spent in response.spents:

        assert isinstance(spent.date, str)

        assert isinstance(spent.description, str)

        assert isinstance(spent.value, str)

        assert re.match(pattern_date, spent.date), f"Invalid spent date  = {spent.date}"

        assert spent.description is not None

        assert re.match(
            pattern_value, spent.value
        ), f"Invalid spent value = {spent.value}"
