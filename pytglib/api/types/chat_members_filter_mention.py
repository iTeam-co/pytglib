

from ..utils import Object


class ChatMembersFilterMention(Object):
    """
    Returns users which can be mentioned in the chat 

    Attributes:
        ID (:obj:`str`): ``ChatMembersFilterMention``

    Args:
        message_thread_id (:obj:`int`):
            If non-zero, the identifier of the current message thread

    Returns:
        ChatMembersFilter

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatMembersFilterMention"

    def __init__(self, message_thread_id, **kwargs):
        
        self.message_thread_id = message_thread_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatMembersFilterMention":
        message_thread_id = q.get('message_thread_id')
        return ChatMembersFilterMention(message_thread_id)
