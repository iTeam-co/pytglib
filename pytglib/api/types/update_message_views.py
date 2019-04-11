

from ..utils import Object


class UpdateMessageViews(Object):
    """
    The view count of the message has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateMessageViews``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        message_id (:obj:`int`):
            Message identifier 
        views (:obj:`int`):
            New value of the view count

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateMessageViews"

    def __init__(self, chat_id, message_id, views, **kwargs):
        
        self.chat_id = chat_id  # int
        self.message_id = message_id  # int
        self.views = views  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateMessageViews":
        chat_id = q.get('chat_id')
        message_id = q.get('message_id')
        views = q.get('views')
        return UpdateMessageViews(chat_id, message_id, views)
