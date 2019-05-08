

from ..utils import Object


class NotificationTypeNewPushMessage(Object):
    """
    New message was received through a push notification

    Attributes:
        ID (:obj:`str`): ``NotificationTypeNewPushMessage``

    Args:
        message_id (:obj:`int`):
            The message identifierThe message will not be available in the chat history, but the ID can be used in viewMessages and as reply_to_message_id
        sender_user_id (:obj:`int`):
            Sender of the messageCorresponding user may be inaccessible 
        content (:class:`telegram.api.types.PushMessageContent`):
            Push message content

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewPushMessage"

    def __init__(self, message_id, sender_user_id, content, **kwargs):
        
        self.message_id = message_id  # int
        self.sender_user_id = sender_user_id  # int
        self.content = content  # PushMessageContent

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewPushMessage":
        message_id = q.get('message_id')
        sender_user_id = q.get('sender_user_id')
        content = Object.read(q.get('content'))
        return NotificationTypeNewPushMessage(message_id, sender_user_id, content)
