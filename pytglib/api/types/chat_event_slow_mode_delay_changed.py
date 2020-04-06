

from ..utils import Object


class ChatEventSlowModeDelayChanged(Object):
    """
    The slow_mode_delay setting of a supergroup was changed 

    Attributes:
        ID (:obj:`str`): ``ChatEventSlowModeDelayChanged``

    Args:
        old_slow_mode_delay (:obj:`int`):
            Previous value of slow_mode_delay 
        new_slow_mode_delay (:obj:`int`):
            New value of slow_mode_delay

    Returns:
        ChatEventAction

    Raises:
        :class:`telegram.Error`
    """
    ID = "chatEventSlowModeDelayChanged"

    def __init__(self, old_slow_mode_delay, new_slow_mode_delay, **kwargs):
        
        self.old_slow_mode_delay = old_slow_mode_delay  # int
        self.new_slow_mode_delay = new_slow_mode_delay  # int

    @staticmethod
    def read(q: dict, *args) -> "ChatEventSlowModeDelayChanged":
        old_slow_mode_delay = q.get('old_slow_mode_delay')
        new_slow_mode_delay = q.get('new_slow_mode_delay')
        return ChatEventSlowModeDelayChanged(old_slow_mode_delay, new_slow_mode_delay)
