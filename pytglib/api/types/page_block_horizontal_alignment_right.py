

from ..utils import Object


class PageBlockHorizontalAlignmentRight(Object):
    """
    The content must be right-aligned

    Attributes:
        ID (:obj:`str`): ``PageBlockHorizontalAlignmentRight``

    No parameters required.

    Returns:
        PageBlockHorizontalAlignment

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockHorizontalAlignmentRight"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockHorizontalAlignmentRight":
        
        return PageBlockHorizontalAlignmentRight()
