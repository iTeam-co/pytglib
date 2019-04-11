

from ..utils import Object


class MessageChatChangePhoto(Object):
    """
    An updated chat photo 

    Attributes:
        ID (:obj:`str`): ``MessageChatChangePhoto``

    Args:
        photo (:class:`telegram.api.types.photo`):
            New chat photo

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageChatChangePhoto"

    def __init__(self, photo, **kwargs):
        
        self.photo = photo  # Photo

    @staticmethod
    def read(q: dict, *args) -> "MessageChatChangePhoto":
        photo = Object.read(q.get('photo'))
        return MessageChatChangePhoto(photo)
