from pytest_asserters.asserters import assert_json_equal


class TestJsonAsserters:
    def test_json_equal(self, expected_simple_json):
        """Test if 2 JSON objects are equal"""
        assert_json_equal(left=expected_simple_json, right=expected_simple_json)
