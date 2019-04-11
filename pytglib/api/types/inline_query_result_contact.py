

from ..utils import Object


class InlineQueryResultContact(Object):
    """
    Represents a user contact 

    Attributes:
        ID (:obj:`str`): ``InlineQueryResultContact``

    Args:
        id (:obj:`str`):
            Unique identifier of the query result 
        contact (:class:`telegram.api.types.contact`):
            A user contact 
        thumbnail (:class:`telegram.api.types.photoSize`):
            Result thumbnail; may be null

    Returns:
        InlineQueryResult

    Raises:
        :class:`telegram.Error`
    """
    ID = "inlineQueryResultContact"

    def __init__(self, id, contact, thumbnail, **kwargs):
        
        self.id = id  # str
        self.contact = contact  # Contact
        self.thumbnail = thumbnail  # PhotoSize

    @staticmethod
    def read(q: dict, *args) -> "InlineQueryResultContact":
        id = q.get('id')
        contact = Object.read(q.get('contact'))
        thumbnail = Object.read(q.get('thumbnail'))
        return InlineQueryResultContact(id, contact, thumbnail)
