

from ..utils import Object


class UpdateMessageInteractionInfo(Object):
    """
    The information about interactions with a message has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageInteractionInfo``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        interaction_info (:class:`telegram.api.types.messageInteractionInfo`):
            New information about interactions with the message; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageInteractionInfo"

    def __init__(self, chat_id, message_id, interaction_info, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.interaction_info = interaction_info  # MessageInteractionInfo

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageInteractionInfo":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        interaction_info = Object.read(q.get('interaction_info'))
        return UpdateMessageInteractionInfo(chat_id, message_id, interaction_info)
