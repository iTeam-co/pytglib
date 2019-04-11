

from ..utils import Object


class InlineQueryResultSticker(Object):
    """
    Represents a sticker 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultSticker``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        sticker (:class:`telegram.api.types.sticker`):
            Sticker

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultSticker"

    def __init__(self, id, sticker, **kwargs):
        
        self.id = id  # str
        self.sticker = sticker  # Sticker

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultSticker":
        id = q.get('id')
        sticker = Object.read(q.get('sticker'))
        return InlineQueryResultSticker(id, sticker)
