

from ..utils import Object


class PageBlockVerticalAlignmentBottom(Object):
    """
    The content should be bottom-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockVerticalAlignmentBottom``

    No parameters required.

    Returns:
        PageBlockVerticalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockVerticalAlignmentBottom"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVerticalAlignmentBottom":
        
        return PageBlockVerticalAlignmentBottom()
