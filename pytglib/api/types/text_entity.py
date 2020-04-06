

from ..utils import Object


class TextEntity(Object):
    """
    Represents a part of the text that needs to be formatted in some unusual way 

    Attributes:
        ID (:obj:`str`): ``TextEntity``

    Args:
        offset (:obj:`int`):
            Offset of the entity in UTF-16 code units 
        length (:obj:`int`):
            Length of the entity, in UTF-16 code units 
        type (:class:`telegram.api.types.TextEntityType`):
            Type of the entity

    Returns:
        TextEntity

    Raises:
        :class:`telegram.Error`
    """
    ID = "textEntity"

    def __init__(self, offset, length, type, **kwargs):
        
        self.offset = offset  # int
        self.length = length  # int
        self.type = type  # TextEntityType

    @staticmethod
    def read(q: dict, *args) -> "TextEntity":
        offset = q.get('offset')
        length = q.get('length')
        type = Object.read(q.get('type'))
        return TextEntity(offset, length, type)
