

from ..utils import Object


class PageBlockVerticalAlignment(Object):
    """
    Describes a Vertical alignment of a table cell content

    No parameters required.
    """
    ID = "pageBlockVerticalAlignment"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVerticalAlignmentMiddle or PageBlockVerticalAlignmentTop or PageBlockVerticalAlignmentBottom":
        if q.get("@type"):
            return Object.read(q)
        return PageBlockVerticalAlignment()
