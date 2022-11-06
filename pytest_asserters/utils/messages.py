import pprint
from typing import Dict, List, Optional, Tuple, Union

pp = pprint.PrettyPrinter(indent=4)


class AssertErrorMessages:
    """Class to refactor all assertion messages"""

    def json_not_equal(
        self, left: dict, right: dict, diffs: Optional[Union[List, Dict, Tuple]]
    ) -> str:
        """
        Return message when 2 JSON/dictionary objects are not equal

        Parameters
        ----------
        left : dict
            Left handside objects, usually the expected objects
        right : dict
            Right handside objects, usually the actual objects
        diffs : dict
            Differences found

        Returns
        -------
        str
            The message to be displayed
        """

        return f"""
            JSON objects are not equal
            Left:
                {pp.pformat(left)}
            Right:
                {pp.pformat(right)}
            Differences:
                {pp.pformat(diffs)}
        """


msg = AssertErrorMessages()
