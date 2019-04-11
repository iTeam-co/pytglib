

from ..utils import Object


class PageBlockBlockQuote(Object):
    """
    A block quote 

    Attributes:
        ID (:obj:`str`): ``PageBlockBlockQuote``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Quote text 
        caption (:class:`telegram.api.types.RichText`):
            Quote caption

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockBlockQuote"

    def __init__(self, text, caption, **kwargs):
        
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockBlockQuote":
        text = Object.read(q.get('text'))
        caption = Object.read(q.get('caption'))
        return PageBlockBlockQuote(text, caption)
