

from ..utils import Object


class ChatEventMessageUnpinned(Object):
    """
    A message was unpinned

    Attributes:
        ID (:obj:`str`): ``ChatEventMessageUnpinned``

    No parameters required.

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventMessageUnpinned"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "ChatEventMessageUnpinned":
        
        return ChatEventMessageUnpinned()
