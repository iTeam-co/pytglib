

from ..utils import Object


class LoginUrlInfo(Object):
    """
    Contains information about an inline button of type inlineKeyboardButtonTypeLoginUrl

    No parameters required.
    """
    ID = "loginUrlInfo"

    def __init__(self, **kwargs):
        
        pass

    @staticmethod
    def read(q: dict, *args) -> "LoginUrlInfoRequestConfirmation or LoginUrlInfoOpen":
        if q.get("@type"):
            return Object.read(q)
        return LoginUrlInfo()
