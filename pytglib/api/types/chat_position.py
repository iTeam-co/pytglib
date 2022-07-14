

from ..utils import Object


class ChatPosition(Object):
    """
    Describes a position of a chat in a chat list

    Attributes:
        ID (:obj:`str`): ``ChatPosition``

    Args:
        list (:class:`telegram.api.types.ChatList`):
            The chat list
        order (:obj:`int`):
            A parameter used to determine order of the chat in the chat listChats must be sorted by the pair (order, chatid) in descending order
        is_pinned (:obj:`bool`):
            True, if the chat is pinned in the chat list
        source (:class:`telegram.api.types.ChatSource`):
            Source of the chat in the chat list; may be null

    Returns:
        ChatPosition

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatPosition"

    def __init__(self, list, order, is_pinned, source, **kwargs):
        
        self.list = list  # ChatList
        self.order = order  # int
        self.is_pinned = is_pinned  # bool
        self.source = source  # ChatSource

    @staticmethod
    def read(q: dict, *args) -> "ChatPosition":
        list = Object.read(q.get('list'))
        order = q.get('order')
        is_pinned = q.get('is_pinned')
        source = Object.read(q.get('source'))
        return ChatPosition(list, order, is_pinned, source)
