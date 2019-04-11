

from ..utils import Object


class PageBlockSubtitle(Object):
    """
    The subtitle of a page 

    Attributes:
        ID (:obj:`str`): ``PageBlockSubtitle``

    Args:
        subtitle (:class:`telegram.api.types.RichText`):
            Subtitle

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockSubtitle"

    def __init__(self, subtitle, **kwargs):
        
        self.subtitle = subtitle  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockSubtitle":
        subtitle = Object.read(q.get('subtitle'))
        return PageBlockSubtitle(subtitle)
