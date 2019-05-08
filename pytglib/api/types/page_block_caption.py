

from ..utils import Object


class PageBlockCaption(Object):
    """
    Contains a caption of an instant view web page block, consisting of a text and a trailing credit 

    Attributes:
        ID (:obj:`str`): ``PageBlockCaption``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Content of the caption 
        credit (:class:`telegram.api.types.RichText`):
            Block credit (like HTML tag <cite>)

    Returns:
        PageBlockCaption

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockCaption"

    def __init__(self, text, credit, **kwargs):
        
        self.text = text  # RichText
        self.credit = credit  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockCaption":
        text = Object.read(q.get('text'))
        credit = Object.read(q.get('credit'))
        return PageBlockCaption(text, credit)
