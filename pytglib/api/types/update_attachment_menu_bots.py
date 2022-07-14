

from ..utils import Object


class UpdateAttachmentMenuBots(Object):
    """
    The list of bots added to attachment menu has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateAttachmentMenuBots``

    Args:
        bots (List of :class:`telegram.api.types.attachmentMenuBot`):
            The new list of bots added to attachment menuThe bots must not be shown on scheduled messages screen

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateAttachmentMenuBots"

    def __init__(self, bots, **kwargs):
        
        self.bots = bots  # list of attachmentMenuBot

    @staticmethod
    def read(q: dict, *args) -> "UpdateAttachmentMenuBots":
        bots = [Object.read(i) for i in q.get('bots', [])]
        return UpdateAttachmentMenuBots(bots)
