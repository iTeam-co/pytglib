

from ..utils import Object


class MessageSendingStateFailed(Object):
    """
    The message failed to be sent 

    Attributes:
        ID (:obj:`str`): ``MessageSendingStateFailed``

    Args:
        error_code (:obj:`int`):
            An error code; 0 if unknown 
        error_message (:obj:`str`):
            Error message
        can_retry (:obj:`bool`):
            True, if the message can be re-sent 
        retry_after (:obj:`float`):
            Time left before the message can be re-sent, in secondsNo update is sent when this field changes

    Returns:
        MessageSendingState

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageSendingStateFailed"

    def __init__(self, error_code, error_message, can_retry, retry_after, **kwargs):
        
        self.error_code = error_code  # int
        self.error_message = error_message  # str
        self.can_retry = can_retry  # bool
        self.retry_after = retry_after  # float

    @staticmethod
    def read(q: dict, *args) -> "MessageSendingStateFailed":
        error_code = q.get('error_code')
        error_message = q.get('error_message')
        can_retry = q.get('can_retry')
        retry_after = q.get('retry_after')
        return MessageSendingStateFailed(error_code, error_message, can_retry, retry_after)
