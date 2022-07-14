

from ..utils import Object


class GetChatSponsoredMessage(Object):
    """
    Returns sponsored message to be shown in a chat; for channel chats only. Returns a 404 error if there is no sponsored message in the chat 

    Attributes:
        ID (:obj:`str`): ``GetChatSponsoredMessage``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat

    Returns:
        SponsoredMessage

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatSponsoredMessage"

    def __init__(self, chat_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "GetChatSponsoredMessage":
        chat_id = q.get('chat_id')
        return GetChatSponsoredMessage(chat_id)
