

from ..utils import Object


class TextEntityTypeTextUrl(Object):
    """
    A text description shown instead of a raw URL 

    Attributes:
        ID (:obj:`str`): ``TextEntityTypeTextUrl``

    Args:
        url (:obj:`str`):
            HTTP or tg:// URL to be opened when the link is clicked

    Returns:
        TextEntityType

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntityTypeTextUrl"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "TextEntityTypeTextUrl":
        url = q.get('url')
        return TextEntityTypeTextUrl(url)
