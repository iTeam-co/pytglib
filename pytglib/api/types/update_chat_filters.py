

from ..utils import Object


class UpdateChatFilters(Object):
    """
    The list of chat filters or a chat filter has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatFilters``

    Args:
        chat_filters (List of :class:`telegram.api.types.chatFilterInfo`):
            The new list of chat filters 
        main_chat_list_position (:obj:`int`):
            Position of the main chat list among chat filters, 0-based

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatFilters"

    def __init__(self, chat_filters, main_chat_list_position, **kwargs):
        
        self.chat_filters = chat_filters  # list of chatFilterInfo
        self.main_chat_list_position = main_chat_list_position  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatFilters":
        chat_filters = [Object.read(i) for i in q.get('chat_filters', [])]
        main_chat_list_position = q.get('main_chat_list_position')
        return UpdateChatFilters(chat_filters, main_chat_list_position)
