

from ..utils import Object


class SendPassportAuthorizationForm(Object):
    """
    Sends a Telegram Passport authorization form, effectively sharing data with the service. This method must be called after getPassportAuthorizationFormAvailableElements if some previously available elements need to be used

    Attributes:
        ID (:obj:`str`): ``SendPassportAuthorizationForm``

    Args:
        autorization_form_id (:obj:`int`):
            Authorization form identifier 
        types (List of :class:`telegram.api.types.PassportElementType`):
            Types of Telegram Passport elements chosen by user to complete the authorization form

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "sendPassportAuthorizationForm"

    def __init__(self, autorization_form_id, types, extra=None, **kwargs):
        self.extra = extra
        self.autorization_form_id = autorization_form_id  # int
        self.types = types  # list of PassportElementType

    @staticmethod
    def read(q: dict, *args) -> "SendPassportAuthorizationForm":
        autorization_form_id = q.get('autorization_form_id')
        types = [Object.read(i) for i in q.get('types', [])]
        return SendPassportAuthorizationForm(autorization_form_id, types)
