

from ..utils import Object


class DeleteSavedCredentials(Object):
    """
    Deletes saved credentials for all payment provider bots

    Attributes:
        ID (:obj:`str`): ``DeleteSavedCredentials``

    No parameters required.

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteSavedCredentials"

    def __init__(self, extra=None, **kwargs):
        self.extra = extra
        pass

    @staticmethod
    def read(q: dict, *args) -> "DeleteSavedCredentials":
        
        return DeleteSavedCredentials()
