

from ..utils import Object


class UpdateChatChatList(Object):
    """
    The list to which the chat belongs was changed. This update is guaranteed to be sent only when chat.order == 0 and the current or the new chat list is null 

    Attributes:
        ID (:obj:`str`): ``UpdateChatChatList``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        chat_list (:class:`telegram.api.types.ChatList`):
            The new chat's chat list; may be null

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatChatList"

    def __init__(self, chat_id, chat_list, **kwargs):
        
        self.chat_id = chat_id  # int
        self.chat_list = chat_list  # ChatList

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatChatList":
        chat_id = q.get('chat_id')
        chat_list = Object.read(q.get('chat_list'))
        return UpdateChatChatList(chat_id, chat_list)
