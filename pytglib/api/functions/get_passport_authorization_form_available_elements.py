

from ..utils import Object


class GetPassportAuthorizationFormAvailableElements(Object):
    """
    Returns already available Telegram Passport elements suitable for completing a Telegram Passport authorization form. Result can be received only once for each authorization form 

    Attributes:
        ID (:obj:`str`): ``GetPassportAuthorizationFormAvailableElements``

    Args:
        autorization_form_id (:obj:`int`):
            Authorization form identifier 
        password (:obj:`str`):
            Password of the current user

    Returns:
        PassportElementsWithErrors

    Raises:
        :class:`telegram.Error`
    """
    ID = "getPassportAuthorizationFormAvailableElements"

    def __init__(self, autorization_form_id, password, extra=None, **kwargs):
        self.extra = extra
        self.autorization_form_id = autorization_form_id  # int
        self.password = password  # str

    @staticmethod
    def read(q: dict, *args) -> "GetPassportAuthorizationFormAvailableElements":
        autorization_form_id = q.get('autorization_form_id')
        password = q.get('password')
        return GetPassportAuthorizationFormAvailableElements(autorization_form_id, password)
