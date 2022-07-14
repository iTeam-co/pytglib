

from ..utils import Object


class EditChatFilter(Object):
    """
    Edits existing chat filter. Returns information about the edited chat filter 

    Attributes:
        ID (:obj:`str`): ``EditChatFilter``

    Args:
        chat_filter_id (:obj:`int`):
            Chat filter identifier 
        filter (:class:`telegram.api.types.chatFilter`):
            The edited chat filter

    Returns:
        ChatFilterInfo

    Raises:
        :class:`telegram.Error`
    """
    ID = "editChatFilter"

    def __init__(self, chat_filter_id, filter, extra=None, **kwargs):
        self.extra = extra
        self.chat_filter_id = chat_filter_id  # int
        self.filter = filter  # ChatFilter

    @staticmethod
    def read(q: dict, *args) -> "EditChatFilter":
        chat_filter_id = q.get('chat_filter_id')
        filter = Object.read(q.get('filter'))
        return EditChatFilter(chat_filter_id, filter)
