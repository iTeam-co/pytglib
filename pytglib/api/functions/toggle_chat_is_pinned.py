

from ..utils import Object


class ToggleChatIsPinned(Object):
    """
    Changes the pinned state of a chat. There can be up to GetOption("pinned_chat_count_max")/GetOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium

    Attributes:
        ID (:obj:`str`): ``ToggleChatIsPinned``

    Args:
        chat_list (:class:`telegram.api.types.ChatList`):
            Chat list in which to change the pinned state of the chat 
        chat_id (:obj:`int`):
            Chat identifier 
        is_pinned (:obj:`bool`):
            Pass true to pin the chat; pass false to unpin it

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "toggleChatIsPinned"

    def __init__(self, chat_list, chat_id, is_pinned, extra=None, **kwargs):
        self.extra = extra
        self.chat_list = chat_list  # ChatList
        self.chat_id = chat_id  # int
        self.is_pinned = is_pinned  # bool

    @staticmethod
    def read(q: dict, *args) -> "ToggleChatIsPinned":
        chat_list = Object.read(q.get('chat_list'))
        chat_id = q.get('chat_id')
        is_pinned = q.get('is_pinned')
        return ToggleChatIsPinned(chat_list, chat_id, is_pinned)
