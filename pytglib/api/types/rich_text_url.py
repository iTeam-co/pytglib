

from ..utils import Object


class RichTextUrl(Object):
    """
    A rich text URL link 

    Attributes:
        ID (:obj:`str`): ``RichTextUrl``

    Args:
        text (:class:`telegram.api.types.RichText`):
            Text 
        url (:obj:`str`):
            URL

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextUrl"

    def __init__(self, text, url, **kwargs):
        
        self.text = text  # RichText
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "RichTextUrl":
        text = Object.read(q.get('text'))
        url = q.get('url')
        return RichTextUrl(text, url)
