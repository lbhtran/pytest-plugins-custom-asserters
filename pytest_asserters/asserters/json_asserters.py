from typing import Dict, List, Optional, Tuple, Union

from jsondiff import diff

from pytest_asserters.utils.messages import msg


def assert_json_equal(
    left: dict, right: dict, ignore_fields: Optional[List[str]] = None
) -> None:
    """
    An asserter to compare if 2 JSON objects are equal

    Parameters
    ----------
    left : dict
        Left-hand side of the comparison
    right : dict
        Right-hand side of the comparison
    ignore_fields : Optional[List[str]]
        List of fields to ignore. This is often used when there are randomly
        generated fields like `created_date`, `uuid`, ...`

    Returns
    -------
    None
        This function doesn't return anything when successfully runs. If the
        objects are not equal, an AssertionError will be raised

    Raises
    ------
    AssertionError:
        Print the left and righ objects and their differences if any
    """

    if ignore_fields:
        for field in ignore_fields:
            if field in left:
                del left[field]
            if field in right:
                del right[field]

    diffs: Optional[Union[List, Dict, Tuple]] = diff(left, right, syntax="symmetric")

    if left != right:
        raise AssertionError(msg.json_not_equal(left=left, right=right, diffs=diffs))
