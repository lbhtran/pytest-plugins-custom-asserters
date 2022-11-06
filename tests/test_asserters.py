import pytest

from pytest_asserters.asserters import assert_json_equal


class TestJsonAsserters:
    def test_simple_json_equal(self, simple_json):
        """Test if 2 simple JSON objects are equal"""
        assert_json_equal(left=simple_json, right=simple_json)

    def test_json_not_equal(self, simple_json, different_simple_json, simple_json_diff):
        """Test if correct assertion error is raised when 2 simple JSON objects are not equal"""

        with pytest.raises(AssertionError) as exc:
            assert_json_equal(left=simple_json, right=different_simple_json)

        assert exc.value.args[0] == simple_json_diff
