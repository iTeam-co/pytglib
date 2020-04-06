

from ..utils import Object


class UpdateNewInlineQuery(Object):
    """
    A new incoming inline query; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewInlineQuery``

    Args:
        id (:obj:`int`):
            Unique query identifier 
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query 
        user_location (:class:`telegram.api.types.location`):
            User location, provided by the client; may be null
        query (:obj:`str`):
            Text of the query 
        offset (:obj:`str`):
            Offset of the first entry to return

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewInlineQuery"

    def __init__(self, id, sender_user_id, user_location, query, offset, **kwargs):
        
        self.id = id  # int
        self.sender_user_id = sender_user_id  # int
        self.user_location = user_location  # Location
        self.query = query  # str
        self.offset = offset  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewInlineQuery":
        id = q.get('id')
        sender_user_id = q.get('sender_user_id')
        user_location = Object.read(q.get('user_location'))
        query = q.get('query')
        offset = q.get('offset')
        return UpdateNewInlineQuery(id, sender_user_id, user_location, query, offset)
