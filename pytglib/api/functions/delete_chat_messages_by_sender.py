

from ..utils import Object


class DeleteChatMessagesBySender(Object):
    """
    Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges 

    Attributes:
        ID (:obj:`str`): ``DeleteChatMessagesBySender``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of the sender of messages to delete

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteChatMessagesBySender"

    def __init__(self, chat_id, sender_id, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.sender_id = sender_id  # MessageSender

    @staticmethod
    def read(q: dict, *args) -> "DeleteChatMessagesBySender":
        chat_id = q.get('chat_id')
        sender_id = Object.read(q.get('sender_id'))
        return DeleteChatMessagesBySender(chat_id, sender_id)
