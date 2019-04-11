

from ..utils import Object


class UpdateNewMessage(Object):
    """
    A new message was received; can also be an outgoing message 

    Attributes:
        ID (:obj:`str`): ``UpdateNewMessage``

    Args:
        message (:class:`telegram.api.types.message`):
            The new message 
        disable_notification (:obj:`bool`):
            True, if this message must not generate a notification 
        contains_mention (:obj:`bool`):
            True, if the message contains a mention of the current user

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateNewMessage"

    def __init__(self, message, disable_notification, contains_mention, **kwargs):
        
        self.message = message  # Message
        self.disable_notification = disable_notification  # bool
        self.contains_mention = contains_mention  # bool

    @staticmethod
    def read(q: dict, *args) -> "UpdateNewMessage":
        message = Object.read(q.get('message'))
        disable_notification = q.get('disable_notification')
        contains_mention = q.get('contains_mention')
        return UpdateNewMessage(message, disable_notification, contains_mention)
