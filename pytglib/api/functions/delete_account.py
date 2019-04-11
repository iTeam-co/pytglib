

from ..utils import Object


class DeleteAccount(Object):
    """
    Deletes the account of the current user, deleting all information associated with the user from the server. The phone number of the account can be used to create a new account. Can be called before authorization when the current authorization state is authorizationStateWaitPassword 

    Attributes:
        ID (:obj:`str`): ``DeleteAccount``

    Args:
        reason (:obj:`str`):
            The reason why the account was deleted; optional

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "deleteAccount"

    def __init__(self, reason, extra=None, **kwargs):
        self.extra = extra
        self.reason = reason  # str

    @staticmethod
    def read(q: dict, *args) -> "DeleteAccount":
        reason = q.get('reason')
        return DeleteAccount(reason)
