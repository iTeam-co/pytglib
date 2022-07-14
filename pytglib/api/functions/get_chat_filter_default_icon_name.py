

from ..utils import Object


class GetChatFilterDefaultIconName(Object):
    """
    Returns default icon name for a filter. Can be called synchronously 

    Attributes:
        ID (:obj:`str`): ``GetChatFilterDefaultIconName``

    Args:
        filter (:class:`telegram.api.types.chatFilter`):
            Chat filter

    Returns:
        Text

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatFilterDefaultIconName"

    def __init__(self, filter, extra=None, **kwargs):
        self.extra = extra
        self.filter = filter  # ChatFilter

    @staticmethod
    def read(q: dict, *args) -> "GetChatFilterDefaultIconName":
        filter = Object.read(q.get('filter'))
        return GetChatFilterDefaultIconName(filter)
