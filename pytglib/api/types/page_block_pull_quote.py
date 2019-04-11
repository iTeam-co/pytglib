

from ..utils import Object


class PageBlockPullQuote(Object):
    """
    A pull quote 

    Attributes:
        ID (:obj:`str`): ``PageBlockPullQuote``

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
    ID = "pageBlockPullQuote"

    def __init__(self, text, caption, **kwargs):
        
        self.text = text  # RichText
        self.caption = caption  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockPullQuote":
        text = Object.read(q.get('text'))
        caption = Object.read(q.get('caption'))
        return PageBlockPullQuote(text, caption)
