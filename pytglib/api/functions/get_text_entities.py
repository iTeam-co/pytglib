

from ..utils import Object


class GetTextEntities(Object):
    """
    Returns all entities (mentions, hashtags, cashtags, bot commands, bank card numbers, URLs, and email addresses) contained in the text. This is an offline method. Can be called before authorization. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetTextEntities``

    Args:
        text (:obj:`str`):
            The text in which to look for entites

    Returns:
        TextEntities

    Raises:
        :class:`telegram.Error`
    """
    ID = "getTextEntities"

    def __init__(self, text, extra=None, **kwargs):
        self.extra = extra
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "GetTextEntities":
        text = q.get('text')
        return GetTextEntities(text)
