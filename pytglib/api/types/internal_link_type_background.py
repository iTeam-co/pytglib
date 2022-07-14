

from ..utils import Object


class InternalLinkTypeBackground(Object):
    """
    The link is a link to a background. Call searchBackground with the given background name to process the link 

    Attributes:
        ID (:obj:`str`): ``InternalLinkTypeBackground``

    Args:
        background_name (:obj:`str`):
            Name of the background

    Returns:
        InternalLinkType

    Raises:
        :class:`telegram.Error`
    """
    ID = "internalLinkTypeBackground"

    def __init__(self, background_name, **kwargs):
        
        self.background_name = background_name  # str

    @staticmethod
    def read(q: dict, *args) -> "InternalLinkTypeBackground":
        background_name = q.get('background_name')
        return InternalLinkTypeBackground(background_name)
