

from ..utils import Object


class UpdateChatAction(Object):
    """
    A message sender activity in the chat has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatAction``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_thread_id (:obj:`int`):
            If not 0, a message thread identifier in which the action was performed 
        sender_id (:class:`telegram.api.types.MessageSender`):
            Identifier of a message sender performing the action 
        action (:class:`telegram.api.types.ChatAction`):
            The action

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatAction"

    def __init__(self, chat_id, message_thread_id, sender_id, action, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_thread_id = message_thread_id  # int
        self.sender_id = sender_id  # MessageSender
        self.action = action  # ChatAction

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatAction":
        chat_id = q.get('chat_id')
        message_thread_id = q.get('message_thread_id')
        sender_id = Object.read(q.get('sender_id'))
        action = Object.read(q.get('action'))
        return UpdateChatAction(chat_id, message_thread_id, sender_id, action)
