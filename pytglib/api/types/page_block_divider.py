

from ..utils import Object


class PageBlockDivider(Object):
    """
    An empty block separating a page

    Attributes:
        ID (:obj:`str`): ``PageBlockDivider``

    No parameters required.

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockDivider"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "PageBlockDivider":
        
        return PageBlockDivider()
