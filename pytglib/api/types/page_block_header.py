

from ..utils import Object


class PageBlockHeader(Object):
    """
    A header 

    Attributes:
        ID (:obj:`str`): ``PageBlockHeader``

    Args:
        header (:class:`telegram.api.types.RichText`):
            Header

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockHeader"

    def __init__(self, header, **kwargs):
        
        self.header = header  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockHeader":
        header = Object.read(q.get('header'))
        return PageBlockHeader(header)
