

from ..utils import Object


class SetChatLocation(Object):
    """
    Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use 

    Attributes:
        ID (:obj:`str`): ``SetChatLocation``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        location (:class:`telegram.api.types.chatLocation`):
            New location for the chat; must be valid and not null

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatLocation"

    def __init__(self, chat_id, location, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.location = location  # ChatLocation

    @staticmethod
    def read(q: dict, *args) -> "SetChatLocation":
        chat_id = q.get('chat_id')
        location = Object.read(q.get('location'))
        return SetChatLocation(chat_id, location)
