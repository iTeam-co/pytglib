

from ..utils import Object


class SetChatSlowModeDelay(Object):
    """
    Changes the slow mode delay of a chat. Available only for supergroups; requires can_restrict_members rights 

    Attributes:
        ID (:obj:`str`): ``SetChatSlowModeDelay``

    Args:
        chat_id (:obj:`int`):
            Chat identifier 
        slow_mode_delay (:obj:`int`):
            New slow mode delay for the chat; must be one of 0, 10, 30, 60, 300, 900, 3600

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setChatSlowModeDelay"

    def __init__(self, chat_id, slow_mode_delay, extra=None, **kwargs):
        self.extra = extra
        self.chat_id = chat_id  # int
        self.slow_mode_delay = slow_mode_delay  # int

    @staticmethod
    def read(q: dict, *args) -> "SetChatSlowModeDelay":
        chat_id = q.get('chat_id')
        slow_mode_delay = q.get('slow_mode_delay')
        return SetChatSlowModeDelay(chat_id, slow_mode_delay)
