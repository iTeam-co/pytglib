

from ..utils import Object


class PageBlockAnchor(Object):
    """
    An invisible anchor on a page, which can be used in a URL to open the page from the specified anchor 

    Attributes:
        ID (:obj:`str`): ``PageBlockAnchor``

    Args:
        name (:obj:`str`):
            Name of the anchor

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockAnchor"

    def __init__(self, name, **kwargs):
        
        self.name = name  # str

    @staticmethod
    def read(q: dict, *args) -> "PageBlockAnchor":
        name = q.get('name')
        return PageBlockAnchor(name)
