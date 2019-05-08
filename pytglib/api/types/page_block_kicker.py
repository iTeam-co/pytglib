

from ..utils import Object


class PageBlockKicker(Object):
    """
    A kicker 

    Attributes:
        ID (:obj:`str`): ``PageBlockKicker``

    Args:
        kicker (:class:`telegram.api.types.RichText`):
            Kicker

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockKicker"

    def __init__(self, kicker, **kwargs):
        
        self.kicker = kicker  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockKicker":
        kicker = Object.read(q.get('kicker'))
        return PageBlockKicker(kicker)
