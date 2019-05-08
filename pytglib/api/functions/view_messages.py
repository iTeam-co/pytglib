

from ..utils import Object


class ViewMessages(Object):
    """
    Informs TDLib that messages are being viewed by the user. Many useful activities depend on whether the messages are currently being viewed or not (e.g., marking messages as read, incrementing a view counter, updating a view counter, removing deleted messages in supergroups and channels) 

    Attributes:
        ID (:obj:`str`): ``ViewMessages``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_ids (List of :obj:`int`):
            The identifiers of the messages being viewed
        force_read (:obj:`bool`):
            True, if messages in closed chats should be marked as read

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "viewMessages"

    def __init__(self, chat_id, message_ids, force_read, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.message_ids = message_ids  # list of int
        self.force_read = force_read  # bool

    @staticmethod
    def read(q: dict, *args) -> "ViewMessages":
        chat_id = q.get('chat_id')
        message_ids = q.get('message_ids')
        force_read = q.get('force_read')
        return ViewMessages(chat_id, message_ids, force_read)
