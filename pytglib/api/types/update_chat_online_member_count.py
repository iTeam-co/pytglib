

from ..utils import Object


class UpdateChatOnlineMemberCount(Object):
    """
    The number of online group members has changed. This update with non-zero count is sent only for currently opened chats. There is no guarantee that it will be sent just after the count has changed 

    Attributes:
        ID (:obj:`str`): ``UpdateChatOnlineMemberCount``

    Args:
        chat_id (:obj:`int`):
            Identifier of the chat 
        online_member_count (:obj:`int`):
            New number of online members in the chat, or 0 if unknown

    Returns:
        Update

    Raises:
        :class:`telegram.Error`
    """
    ID = "updateChatOnlineMemberCount"

    def __init__(self, chat_id, online_member_count, **kwargs):
        
        self.chat_id = chat_id  # int
        self.online_member_count = online_member_count  # int

    @staticmethod
    def read(q: dict, *args) -> "UpdateChatOnlineMemberCount":
        chat_id = q.get('chat_id')
        online_member_count = q.get('online_member_count')
        return UpdateChatOnlineMemberCount(chat_id, online_member_count)
