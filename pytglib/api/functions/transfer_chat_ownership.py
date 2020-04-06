

from ..utils import Object


class TransferChatOwnership(Object):
    """
    Changes the owner of a chat. The current user must be a current owner of the chat. Use the method canTransferOwnership to check whether the ownership can be transferred from the current session. Available only for supergroups and channel chats

    Attributes:
        ID (:obj:`str`): ``TransferChatOwnership``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        user_id (:obj:`int`):
            Identifier of the user to which transfer the ownershipThe ownership can't be transferred to a bot or to a deleted user 
        password (:obj:`str`):
            The password of the current user

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "transferChatOwnership"

    def __init__(self, chat_id, user_id, password, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.user_id = user_id  # int
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "TransferChatOwnership":
        chat_id = q.get('chat_id')
        user_id = q.get('user_id')
        password = q.get('password')
        return TransferChatOwnership(chat_id, user_id, password)
