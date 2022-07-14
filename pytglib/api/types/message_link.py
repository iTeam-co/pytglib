

from ..utils import Object


class MessageLink(Object):
    """
    Contains an HTTPS link to a message in a supergroup or channel 

    Attributes:
        ID (:obj:`str`): ``MessageLink``

    Args:
        link (:obj:`str`):
            Message link 
        is_public (:obj:`bool`):
            True, if the link will work for non-members of the chat

    Returns:
        MessageLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageLink"

    def __init__(self, link, is_public, **kwargs):
        
        self.link = link  # str
        self.is_public = is_public  # bool

    @staticmethod
    def read(q: dict, *args) -> "MessageLink":
        link = q.get('link')
        is_public = q.get('is_public')
        return MessageLink(link, is_public)
