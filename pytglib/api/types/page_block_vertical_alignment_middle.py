

from ..utils import Object


class PageBlockVerticalAlignmentMiddle(Object):
    """
    The content should be middle-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockVerticalAlignmentMiddle``

    No parameters required.

    Returns:
        PageBlockVerticalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockVerticalAlignmentMiddle"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockVerticalAlignmentMiddle":
        
        return PageBlockVerticalAlignmentMiddle()
