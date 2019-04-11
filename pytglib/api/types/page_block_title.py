

from ..utils import Object


class PageBlockTitle(Object):
    """
    The title of a page 

    Attributes:
        ID (:obj:`str`): ``PageBlockTitle``

    Args:
        title (:class:`telegram.api.types.RichText`):
            Title

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockTitle"

    def __init__(self, title, **kwargs):
        
        self.title = title  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockTitle":
        title = Object.read(q.get('title'))
        return PageBlockTitle(title)
