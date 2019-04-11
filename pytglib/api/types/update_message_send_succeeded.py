

from ..utils import Object


class UpdateMessageSendSucceeded(Object):
    """
    A message has been successfully sent 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageSendSucceeded``

    Args:
        message (:class:`telegram.api.types.message`):
            Information about the sent messageUsually only the message identifier, date, and content are changed, but almost all other fields can also change 
        old_message_id (:obj:`int`):
            The previous temporary message identifier

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageSendSucceeded"

    def __init__(self, message, old_message_id, **kwargs):
        
        self.message = message  # Message
        self.old_message_id = old_message_id  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageSendSucceeded":
        message = Object.read(q.get('message'))
        old_message_id = q.get('old_message_id')
        return UpdateMessageSendSucceeded(message, old_message_id)
