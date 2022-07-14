

from ..utils import Object


class ChatSourcePublicServiceAnnouncement(Object):
    """
    The chat contains a public service announcement 

    Attributes:
        ID (:obj:`str`): ``ChatSourcePublicServiceAnnouncement``

    Args:
        type (:obj:`str`):
            The type of the announcement 
        text (:obj:`str`):
            The text of the announcement

    Returns:
        ChatSource

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatSourcePublicServiceAnnouncement"

    def __init__(self, type, text, **kwargs):
        
        self.type = type  # str
        self.text = text  # str

    @staticmethod
    def read(q: dict, *args) -> "ChatSourcePublicServiceAnnouncement":
        type = q.get('type')
        text = q.get('text')
        return ChatSourcePublicServiceAnnouncement(type, text)
