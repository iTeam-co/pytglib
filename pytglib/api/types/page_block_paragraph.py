

from ..utils import Object


class PageBlockParagraph(Object):
    """
    A text paragraph 

    Attributes:
        ID (:obj:`str`): ``PageBlockParagraph``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Paragraph text

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockParagraph"

    def __init__(self, text, **kwargs):
        
        self.text = text  # RichText

    @staticmethod
    def read(q: dict, *args) -> "PageBlockParagraph":
        text = Object.read(q.get('text'))
        return PageBlockParagraph(text)
