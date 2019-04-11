

from ..utils import Object


class MessageWebsiteConnected(Object):
    """
    The current user has connected a website by logging in using Telegram Login Widget on it 

    Attributes:
        ID (:obj:`str`): ``MessageWebsiteConnected``

    Args:
        domain_name (:obj:`str`):
            Domain name of the connected website

    Returns:
        MessageContent

    Raises:
        :class:`telegram.Error`
    """
    ID = "messageWebsiteConnected"

    def __init__(self, domain_name, **kwargs):
        
        self.domain_name = domain_name  # str

    @staticmethod
    def read(q: dict, *args) -> "MessageWebsiteConnected":
        domain_name = q.get('domain_name')
        return MessageWebsiteConnected(domain_name)
