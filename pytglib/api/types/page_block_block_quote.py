

from ..utils import Object


class PageBlockBlockQuote(Object):
    """
    A block quote 

    Attributes:
        ID (:obj:`str`): ``PageBlockBlockQuote``

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
    ID = "pageBlockBlockQuote"

    def __init__(self, text, credit, **kwargs):
        
        self.text = text  # RichText
        self.credit = credit  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockBlockQuote":
        text = Object.read(q.get('text'))
        credit = Object.read(q.get('credit'))
        return PageBlockBlockQuote(text, credit)
