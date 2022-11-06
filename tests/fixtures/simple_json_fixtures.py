import json

import pytest


@pytest.fixture(scope="function")
def simple_json() -> dict:
    return json.loads(
        """
        {
            "id": 0,
            "shipname": "Rocinante",
            "crew": 5,
            "affinity": null
        }
        """
    )


@pytest.fixture(scope="function")
def different_simple_json() -> dict:
    return json.loads(
        """
        {
            "id": 0,
            "shipname": "Tachi",
            "crew": 5,
            "affinity": "MCRN"
        }
        """
    )


@pytest.fixture(scope="function")
def simple_json_diff() -> str:
    return """
            JSON objects are not equal
            Left:
                {'affinity': None, 'crew': 5, 'id': 0, 'shipname': 'Rocinante'}
            Right:
                {'affinity': 'MCRN', 'crew': 5, 'id': 0, 'shipname': 'Tachi'}
            Differences:
                {'affinity': [None, 'MCRN'], 'shipname': ['Rocinante', 'Tachi']}
        """
