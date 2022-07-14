

from ..utils import Object


class GetChatStatistics(Object):
    """
    Returns detailed statistics about a chat. Currently, this method can be used only for supergroups and channels. Can be used only if supergroupFullInfo.can_get_statistics == true 

    Attributes:
        ID (:obj:`str`): ``GetChatStatistics``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        is_dark (:obj:`bool`):
            Pass true if a dark theme is used by the application

    Returns:
        ChatStatistics

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatStatistics"

    def __init__(self, chat_id, is_dark, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.is_dark = is_dark  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetChatStatistics":
        chat_id = q.get('chat_id')
        is_dark = q.get('is_dark')
        return GetChatStatistics(chat_id, is_dark)
