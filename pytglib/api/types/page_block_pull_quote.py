

from ..utils import Object


class PageBlockPullQuote(Object):
    """
    A pull quote 

    Attributes:
        ID (:obj:`str`): ``PageBlockPullQuote``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Quote text 
        credit (:class:`telegram.api.types.RichText`):
            Quote credit

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockPullQuote"

    def __init__(self, text, credit, **kwargs):
        
        self.text = text  # RichText
        self.credit = credit  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockPullQuote":
        text = Object.read(q.get('text'))
        credit = Object.read(q.get('credit'))
        return PageBlockPullQuote(text, credit)
