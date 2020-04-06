

from ..utils import Object


class ChatEventLinkedChatChanged(Object):
    """
    The linked chat of a supergroup was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventLinkedChatChanged``

    Args:
        old_linked_chat_id (:obj:`int`):
            Previous supergroup linked chat identifier 
        new_linked_chat_id (:obj:`int`):
            New supergroup linked chat identifier

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventLinkedChatChanged"

    def __init__(self, old_linked_chat_id, new_linked_chat_id, **kwargs):
        
        self.old_linked_chat_id = old_linked_chat_id  # int
        self.new_linked_chat_id = new_linked_chat_id  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventLinkedChatChanged":
        old_linked_chat_id = q.get('old_linked_chat_id')
        new_linked_chat_id = q.get('new_linked_chat_id')
        return ChatEventLinkedChatChanged(old_linked_chat_id, new_linked_chat_id)
