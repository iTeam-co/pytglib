

from ..utils import Object


class SetPassportElementErrors(Object):
    """
    Informs the user that some of the elements in their Telegram Passport contain errors; for bots only. The user will not be able to resend the elements, until the errors are fixed 

    Attributes:
        ID (:obj:`str`): ``SetPassportElementErrors``

    Args:
        user_id (:obj:`int`):
            User identifier 
        errors (List of :class:`telegram.api.types.inputPassportElementError`):
            The errors

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "setPassportElementErrors"

    def __init__(self, user_id, errors, extra=None, **kwargs):
        self.extra = extra
        self.user_id = user_id  # int
        self.errors = errors  # list of inputPassportElementError

    @staticmethod
    def read(q: dict, *args) -> "SetPassportElementErrors":
        user_id = q.get('user_id')
        errors = [Object.read(i) for i in q.get('errors', [])]
        return SetPassportElementErrors(user_id, errors)
