

from ..utils import Object


class PageBlockPreformatted(Object):
    """
    A preformatted text paragraph 

    Attributes:
        ID (:obj:`str`): ``PageBlockPreformatted``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Paragraph text 
        language (:obj:`str`):
            Programming language for which the text should be formatted

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockPreformatted"

    def __init__(self, text, language, **kwargs):
        
        self.text = text  # RichText
        self.language = language  # str

    @staticmethod
    def read(q: dict, *args) -> "PageBlockPreformatted":
        text = Object.read(q.get('text'))
        language = q.get('language')
        return PageBlockPreformatted(text, language)
