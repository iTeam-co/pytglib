

from ..utils import Object


class ProcessChatJoinRequest(Object):
    """
    Handles a pending join request in a chat 

    Attributes:
        ID (:obj:`str`): ``ProcessChatJoinRequest``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            Identifier of the user that sent the request 
        approve (:obj:`bool`):
            Pass true to approve the request; pass false to decline it

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "processChatJoinRequest"

    def __init__(self, chat_id, user_id, approve, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.approve = approve  # bool

    @staticmethod
    def read(q: dict, *args) -> "ProcessChatJoinRequest":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        approve = q.get('approve')
        return ProcessChatJoinRequest(chat_id, user_id, approve)
