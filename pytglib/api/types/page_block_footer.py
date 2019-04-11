

from ..utils import Object


class PageBlockFooter(Object):
    """
    The footer of a page 

    Attributes:
        ID (:obj:`str`): ``PageBlockFooter``

    Args:
        footer (:class:`telegram.api.types.RichText`):
            Footer

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockFooter"

    def __init__(self, footer, **kwargs):
        
        self.footer = footer  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockFooter":
        footer = Object.read(q.get('footer'))
        return PageBlockFooter(footer)
