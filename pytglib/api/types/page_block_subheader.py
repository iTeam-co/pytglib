

from ..utils import Object


class PageBlockSubheader(Object):
    """
    A subheader 

    Attributes:
        ID (:obj:`str`): ``PageBlockSubheader``

    Args:
        subheader (:class:`telegram.api.types.RichText`):
            Subheader

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockSubheader"

    def __init__(self, subheader, **kwargs):
        
        self.subheader = subheader  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockSubheader":
        subheader = Object.read(q.get('subheader'))
        return PageBlockSubheader(subheader)
