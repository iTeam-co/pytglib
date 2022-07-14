

from ..utils import Object


class PageBlockChatLink(Object):
    """
    A link to a chat 

    Attributes:
        ID (:obj:`str`): ``PageBlockChatLink``

    Args:
        title (:obj:`str`):
            Chat title 
        photo (:class:`telegram.api.types.chatPhotoInfo`):
            Chat photo; may be null 
        username (:obj:`str`):
            Chat username by which all other information about the chat can be resolved

    Returns:
        PageBlock

    Raises:
        :class:`telegram.Error`
    """
    ID = "pageBlockChatLink"

    def __init__(self, title, photo, username, **kwargs):
        
        self.title = title  # str
        self.photo = photo  # ChatPhotoInfo
        self.username = username  # str

    @staticmethod
    def read(q: dict, *args) -> "PageBlockChatLink":
        title = q.get('title')
        photo = Object.read(q.get('photo'))
        username = q.get('username')
        return PageBlockChatLink(title, photo, username)
