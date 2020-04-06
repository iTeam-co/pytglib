

from ..utils import Object


class UpdateNewChosenInlineResult(Object):
    """
    The user has chosen a result of an inline query; for bots only 

    Attributes:
        ID (:obj:`str`): ``UpdateNewChosenInlineResult``

    Args:
        sender_user_id (:obj:`int`):
            Identifier of the user who sent the query 
        user_location (:class:`telegram.api.types.location`):
            User location, provided by the client; may be null
        query (:obj:`str`):
            Text of the query 
        result_id (:obj:`str`):
            Identifier of the chosen result 
        inline_message_id (:obj:`str`):
            Identifier of the sent inline message, if known

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewChosenInlineResult"

    def __init__(self, sender_user_id, user_location, query, result_id, inline_message_id, **kwargs):
        
        self.sender_user_id = sender_user_id  # int
        self.user_location = user_location  # Location
        self.query = query  # str
        self.result_id = result_id  # str
        self.inline_message_id = inline_message_id  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewChosenInlineResult":
        sender_user_id = q.get('sender_user_id')
        user_location = Object.read(q.get('user_location'))
        query = q.get('query')
        result_id = q.get('result_id')
        inline_message_id = q.get('inline_message_id')
        return UpdateNewChosenInlineResult(sender_user_id, user_location, query, result_id, inline_message_id)
