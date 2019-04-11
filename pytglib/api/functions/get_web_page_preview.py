

from ..utils import Object


class GetWebPagePreview(Object):
    """
    Returns a web page preview by the text of the message. Do not call this function too often. Returns a 404 error if the web page has no preview 

    Attributes:
        ID (:obj:`str`): ``GetWebPagePreview``

    Args:
        text (:class:`telegram.api.types.formattedText`):
            Message text with formatting

    Returns:
        WebPage

    Raises:
        :class:`telegram.Error`
    """
    ID = "getWebPagePreview"

    def __init__(self, text, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # FormattedText

    @staticmethod
    def read(q: dict, *args) -> "GetWebPagePreview":
        text = Object.read(q.get('text'))
        return GetWebPagePreview(text)
