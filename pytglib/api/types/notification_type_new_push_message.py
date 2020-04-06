

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
            Sender of the message; 0 if unknownCorresponding user may be inaccessible
        sender_name (:obj:`str`):
            Name of the sender; can be different from the name of the sender user
        is_outgoing (:obj:`bool`):
            True, if the message is outgoing
        content (:class:`telegram.api.types.PushMessageContent`):
            Push message content

    Returns:
        NotificationType

    Raises:
        :class:`telegram.Error`
    """
    ID = "notificationTypeNewPushMessage"

    def __init__(self, message_id, sender_user_id, sender_name, is_outgoing, content, **kwargs):
        
        self.message_id = message_id  # int
        self.sender_user_id = sender_user_id  # int
        self.sender_name = sender_name  # str
        self.is_outgoing = is_outgoing  # bool
        self.content = content  # PushMessageContent

    @staticmethod
    def read(q: dict, *args) -> "NotificationTypeNewPushMessage":
        message_id = q.get('message_id')
        sender_user_id = q.get('sender_user_id')
        sender_name = q.get('sender_name')
        is_outgoing = q.get('is_outgoing')
        content = Object.read(q.get('content'))
        return NotificationTypeNewPushMessage(message_id, sender_user_id, sender_name, is_outgoing, content)
