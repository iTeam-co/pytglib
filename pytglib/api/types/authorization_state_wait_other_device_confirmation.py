

from ..utils import Object


class AuthorizationStateWaitOtherDeviceConfirmation(Object):
    """
    The user needs to confirm authorization on another logged in device by scanning a QR code with the provided link 

    Attributes:
        ID (:obj:`str`): ``AuthorizationStateWaitOtherDeviceConfirmation``

    Args:
        link (:obj:`str`):
            A tg:// URL for the QR codeThe link will be updated frequently

    Returns:
        AuthorizationState

    Raises:
        :class:`telegram.Error`
    """
    ID = "authorizationStateWaitOtherDeviceConfirmation"

    def __init__(self, link, **kwargs):
        
        self.link = link  # str

    @staticmethod
    def read(q: dict, *args) -> "AuthorizationStateWaitOtherDeviceConfirmation":
        link = q.get('link')
        return AuthorizationStateWaitOtherDeviceConfirmation(link)
