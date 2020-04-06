

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
        is_cached (:obj:`bool`):
            True, if the URL has cached instant view server-side

    Returns:
        RichText

    Raises:
        :class:`telegram.Error`
    """
    ID = "richTextUrl"

    def __init__(self, text, url, is_cached, **kwargs):
        
        self.text = text  # RichText
        self.url = url  # str
        self.is_cached = is_cached  # bool

    @staticmethod
    def read(q: dict, *args) -> "RichTextUrl":
        text = Object.read(q.get('text'))
        url = q.get('url')
        is_cached = q.get('is_cached')
        return RichTextUrl(text, url, is_cached)
