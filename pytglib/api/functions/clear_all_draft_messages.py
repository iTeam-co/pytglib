

from ..utils import Object


class ClearAllDraftMessages(Object):
    """
    Clears draft messages in all chats 

    Attributes:
        ID (:obj:`str`): ``ClearAllDraftMessages``

    Args:
        exclude_secret_chats (:obj:`bool`):
            If true, local draft messages in secret chats will not be cleared

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "clearAllDraftMessages"

    def __init__(self, exclude_secret_chats, extra=None, **kwargs):
        self.extra = extra
        self.exclude_secret_chats = exclude_secret_chats  # bool

    @staticmethod
    def read(q: dict, *args) -> "ClearAllDraftMessages":
        exclude_secret_chats = q.get('exclude_secret_chats')
        return ClearAllDraftMessages(exclude_secret_chats)
