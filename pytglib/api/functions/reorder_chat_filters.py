

from ..utils import Object


class ReorderChatFilters(Object):
    """
    Changes the order of chat filters 

    Attributes:
        ID (:obj:`str`): ``ReorderChatFilters``

    Args:
        chat_filter_ids (List of :obj:`int`):
            Identifiers of chat filters in the new correct order 
        main_chat_list_position (:obj:`int`):
            Position of the main chat list among chat filters, 0-basedCan be non-zero only for Premium users

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "reorderChatFilters"

    def __init__(self, chat_filter_ids, main_chat_list_position, extra=None, **kwargs):
        self.extra = extra
        self.chat_filter_ids = chat_filter_ids  # list of int
        self.main_chat_list_position = main_chat_list_position  # int

    @staticmethod
    def read(q: dict, *args) -> "ReorderChatFilters":
        chat_filter_ids = q.get('chat_filter_ids')
        main_chat_list_position = q.get('main_chat_list_position')
        return ReorderChatFilters(chat_filter_ids, main_chat_list_position)
