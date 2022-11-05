import json

import pytest


@pytest.fixture(scope="function")
def expected_simple_json() -> dict:
    return json.loads(
        """
        {
            "id": 0,
            "shipname": "Rocinante",
            "crew": 5,
            "affinity": "MCRN"
        }
        """
    )
