

from ..utils import Object


class CreateChatFilter(Object):
    """
    Creates new chat filter. Returns information about the created chat filter. There can be up to GetOption("chat_filter_count_max") chat filters, but the limit can be increased with Telegram Premium 

    Attributes:
        ID (:obj:`str`): ``CreateChatFilter``

    Args:
        filter (:class:`telegram.api.types.chatFilter`):
            Chat filter

    Returns:
        ChatFilterInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "createChatFilter"

    def __init__(self, filter, extra=None, **kwargs):
        self.extra = extra
        self.filter = filter  # ChatFilter

    @staticmethod
    def read(q: dict, *args) -> "CreateChatFilter":
        filter = Object.read(q.get('filter'))
        return CreateChatFilter(filter)
