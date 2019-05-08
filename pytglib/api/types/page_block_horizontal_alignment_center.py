

from ..utils import Object


class PageBlockHorizontalAlignmentCenter(Object):
    """
    The content should be center-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockHorizontalAlignmentCenter``

    No parameters required.

    Returns:
        PageBlockHorizontalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockHorizontalAlignmentCenter"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockHorizontalAlignmentCenter":
        
        return PageBlockHorizontalAlignmentCenter()
