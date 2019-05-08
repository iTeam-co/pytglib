

from ..utils import Object


class PageBlockVerticalAlignmentTop(Object):
    """
    The content should be top-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockVerticalAlignmentTop``

    No parameters required.

    Returns:
        PageBlockVerticalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockVerticalAlignmentTop"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVerticalAlignmentTop":
        
        return PageBlockVerticalAlignmentTop()
