

from ..utils import Object


class DeleteAllCallMessages(Object):
    """
    Deletes all call messages 

    Attributes:
        ID (:obj:`str`): ``DeleteAllCallMessages``

    Args:
        revoke (:obj:`bool`):
            Pass true to delete the messages for all users

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteAllCallMessages"

    def __init__(self, revoke, extra=None, **kwargs):
        self.extra = extra
        self.revoke = revoke  # bool

    @staticmethod
    def read(q: dict, *args) -> "DeleteAllCallMessages":
        revoke = q.get('revoke')
        return DeleteAllCallMessages(revoke)
