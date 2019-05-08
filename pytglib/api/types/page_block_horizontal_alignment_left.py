

from ..utils import Object


class PageBlockHorizontalAlignmentLeft(Object):
    """
    The content should be left-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockHorizontalAlignmentLeft``

    No parameters required.

    Returns:
        PageBlockHorizontalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockHorizontalAlignmentLeft"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockHorizontalAlignmentLeft":
        
        return PageBlockHorizontalAlignmentLeft()
