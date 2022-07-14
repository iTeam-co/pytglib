

from ..utils import Object


class RequestQrCodeAuthentication(Object):
    """
    Requests QR code authentication by scanning a QR code on another logged in device. Works only when the current authorization state is authorizationStateWaitPhoneNumber,or if there is no pending authentication query and the current authorization state is authorizationStateWaitCode, authorizationStateWaitRegistration, or authorizationStateWaitPassword

    Attributes:
        ID (:obj:`str`): ``RequestQrCodeAuthentication``

    Args:
        other_user_ids (List of :obj:`int`):
            List of user identifiers of other users currently using the application

    Returns:
        Ok

    Raises:
        :class:`telegram.Error`
    """
    ID = "requestQrCodeAuthentication"

    def __init__(self, other_user_ids, extra=None, **kwargs):
        self.extra = extra
        self.other_user_ids = other_user_ids  # list of int

    @staticmethod
    def read(q: dict, *args) -> "RequestQrCodeAuthentication":
        other_user_ids = q.get('other_user_ids')
        return RequestQrCodeAuthentication(other_user_ids)
