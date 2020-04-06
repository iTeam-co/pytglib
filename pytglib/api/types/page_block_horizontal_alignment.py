

from ..utils import Object


class PageBlockHorizontalAlignment(Object):
    """
    Describes a horizontal alignment of a table cell content

    No parameters required.
    """
    ID = "pageBlockHorizontalAlignment"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockHorizontalAlignmentCenter or PageBlockHorizontalAlignmentLeft or PageBlockHorizontalAlignmentRight":
        if q.get("@type"):
            return Object.read(q)
        return PageBlockHorizontalAlignment()
