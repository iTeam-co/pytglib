

from ..utils import Object


class UpdateMessageSendFailed(Object):
    """
    A message failed to send. Be aware that some messages being sent can be irrecoverably deleted, in which case updateDeleteMessages will be received instead of this update

    Attributes:
        ID (:obj:`str`): ``UpdateMessageSendFailed``

    Args:
        message (:class:`telegram.api.types.message`):
            Contains information about the message which failed to send 
        old_message_id (:obj:`int`):
            The previous temporary message identifier 
        error_code (:obj:`int`):
            An error code 
        error_message (:obj:`str`):
            Error message

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageSendFailed"

    def __init__(self, message, old_message_id, error_code, error_message, **kwargs):
        
        self.message = message  # Message
        self.old_message_id = old_message_id  # int
        self.error_code = error_code  # int
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageSendFailed":
        message = Object.read(q.get('message'))
        old_message_id = q.get('old_message_id')
        error_code = q.get('error_code')
        error_message = q.get('error_message')
        return UpdateMessageSendFailed(message, old_message_id, error_code, error_message)
