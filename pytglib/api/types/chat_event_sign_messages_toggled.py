

from ..utils import Object


class ChatEventSignMessagesToggled(Object):
    """
    The sign_messages setting of a channel was toggled 

    Attributes:
        ID (:obj:`str`): ``ChatEventSignMessagesToggled``

    Args:
        sign_messages (:obj:`bool`):
            New value of sign_messages

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventSignMessagesToggled"

    def __init__(self, sign_messages, **kwargs):
        
        self.sign_messages = sign_messages  # bool

    @staticmethod
    def read(q: dict, *args) -> "ChatEventSignMessagesToggled":
        sign_messages = q.get('sign_messages')
        return ChatEventSignMessagesToggled(sign_messages)
