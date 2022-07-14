

from ..utils import Object


class InternalLinkTypeMessage(Object):
    """
    The link is a link to a Telegram message. Call getMessageLinkInfo with the given URL to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeMessage``

    Args:
        url (:obj:`str`):
            URL to be passed to getMessageLinkInfo

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeMessage"

    def __init__(self, url, **kwargs):
        
        self.url = url  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeMessage":
        url = q.get('url')
        return InternalLinkTypeMessage(url)
