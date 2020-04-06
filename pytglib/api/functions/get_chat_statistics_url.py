

from ..utils import Object


class GetChatStatisticsUrl(Object):
    """
    Returns an HTTP URL with the chat statistics. Currently this method of getting the statistics is disabled and can be deleted in the future 

    Attributes:
        ID (:obj:`str`): ``GetChatStatisticsUrl``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        parameters (:obj:`str`):
            Parameters from "tg://statsrefresh?params=******" link 
        is_dark (:obj:`bool`):
            Pass true if a URL with the dark theme must be returned

    Returns:
        HttpUrl

    Raises:
        :class:`telegram.Error`
    """
    ID = "getChatStatisticsUrl"

    def __init__(self, chat_id, parameters, is_dark, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.parameters = parameters  # str
        self.is_dark = is_dark  # bool

    @staticmethod
    def read(q: dict, *args) -> "GetChatStatisticsUrl":
        chat_id = q.get('chat_id')
        parameters = q.get('parameters')
        is_dark = q.get('is_dark')
        return GetChatStatisticsUrl(chat_id, parameters, is_dark)
