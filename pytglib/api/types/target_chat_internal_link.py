

from ..utils import Object


class TargetChatInternalLink(Object):
    """
    The chat needs to be open with the provided internal link 

    Attributes:
        ID (:obj:`str`): ``TargetChatInternalLink``

    Args:
        link (:class:`telegram.api.types.InternalLinkType`):
            An internal link pointing to the chat

    Returns:
        TargetChat

    Raises:
        :class:`telegram.Error`
    """
    ID = "targetChatInternalLink"

    def __init__(self, link, **kwargs):
        
        self.link = link  # InternalLinkType

    @staticmethod
    def read(q: dict, *args) -> "TargetChatInternalLink":
        link = Object.read(q.get('link'))
        return TargetChatInternalLink(link)
