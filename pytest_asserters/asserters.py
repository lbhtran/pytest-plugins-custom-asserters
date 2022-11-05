import pprint
from typing import List, Optional

from jsondiff import diff

pp = pprint.PrettyPrinter(indent=4)


def assert_json_equal(
    left: dict, right: dict, ignore_fields: Optional[List[str]] = None
) -> None:
    """
    An asserter to compare if 2 JSON objects are equal
        left (dict): Left-hand side of the equation
        right (dict): Right-hand side of the equation
        ignore_fields (List[str]): list of fields to ignore. This is often use
        when there are automatically generated field like created_date, uuid, ...
    """
    if ignore_fields:
        for field in ignore_fields:
            if field in left:
                del left[field]
            if field in right:
                del right[field]

    diffs = diff(left, right, syntax="symmetric")

    msg = f"""
    JSON objects are not equal
    Left: {pp.pformat(left)}
    Right: {pp.pformat(right)}
    Differences: {pp.pformat(diffs)}
    """

    if left != right:
        raise AssertionError(msg)
