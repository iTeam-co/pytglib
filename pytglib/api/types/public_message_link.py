

from ..utils import Object


class PublicMessageLink(Object):
    """
    Contains a public HTTPS link to a message in a supergroup or channel with a username 

    Attributes:
        ID (:obj:`str`): ``PublicMessageLink``

    Args:
        link (:obj:`str`):
            Message link 
        html (:obj:`str`):
            HTML-code for embedding the message

    Returns:
        PublicMessageLink

    Raises:
        :class:`telegram.Error`
    """
    ID = "publicMessageLink"

    def __init__(self, link, html, **kwargs):
        
        self.link = link  # str
        self.html = html  # str

    @staticmethod
    def read(q: dict, *args) -> "PublicMessageLink":
        link = q.get('link')
        html = q.get('html')
        return PublicMessageLink(link, html)
