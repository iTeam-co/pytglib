

from ..utils import Object


class SetBotUpdatesStatus(Object):
    """
    Informs the server about the number of pending bot updates if they haven't been processed for a long time; for bots only 

    Attributes:
        ID (:obj:`str`): ``SetBotUpdatesStatus``

    Args:
        pending_update_count (:obj:`int`):
            The number of pending updates 
        error_message (:obj:`str`):
            The last error message

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setBotUpdatesStatus"

    def __init__(self, pending_update_count, error_message, extra=None, **kwargs):
        self.extra = extra
        self.pending_update_count = pending_update_count  # int
        self.error_message = error_message  # str

    @staticmethod
    def read(q: dict, *args) -> "SetBotUpdatesStatus":
        pending_update_count = q.get('pending_update_count')
        error_message = q.get('error_message')
        return SetBotUpdatesStatus(pending_update_count, error_message)
